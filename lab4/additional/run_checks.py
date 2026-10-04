"""Run the official Mininet topologies with the student's compiled pipeline."""
import sys, os, json, time, subprocess
from pathlib import Path
sys.path.insert(0, '/tutorials/utils')
from run_exercise import ExerciseRunner

exercise=sys.argv[1]
baseline='--baseline' in sys.argv
folder=Path('/tutorials/exercises')/exercise
os.chdir(folder)
evidence=Path('/lab/additional/evidence')
prefix=exercise+('-baseline' if baseline else '')

class CheckedRunner(ExerciseRunner):
    def do_net_cli(self):
        print('\n=== LIVE MININET: '+prefix+' ===', flush=True)
        loss=self.net.pingAll(timeout='1')
        print('PINGALL_LOSS_PERCENT='+str(loss), flush=True)
        assert loss == (100 if baseline else 0), f'Unexpected ping loss: {loss}'
        if baseline:
            return
        print(self.net.get('h1').cmd('ping -c 4 10.0.2.2'), flush=True)
        if exercise=='basic_tunnel':
            self.check_tunnels()

    def check_tunnels(self):
        cases=[('plain_h2','10.0.2.2',None,'h2'),
               ('plain_h3','10.0.3.3',None,'h3'),
               ('tunnel_h2','10.0.2.2',2,'h2'),
               ('tunnel_overrides_ip','10.0.3.3',2,'h2'),
               ('unknown_tunnel','10.0.2.2',99,None)]
        results=[]
        for name,ip,dst,expected in cases:
            processes=[]
            for host in ['h2','h3']:
                path=evidence/f'{name}-{host}.json'
                ready=evidence/f'{name}-{host}.ready'
                if ready.exists(): ready.unlink()
                proc=self.net.get(host).popen(['python3','/lab/additional/sniff_case.py',str(path),str(ready),name],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                processes.append((host,path,ready,proc))
            deadline=time.monotonic()+15
            while not all(r.exists() for _,_,r,_ in processes):
                if time.monotonic()>deadline: raise RuntimeError('Capture did not become ready')
                time.sleep(.05)
            command=f'python3 send.py {ip} {name}' + (f' --dst_id {dst}' if dst is not None else '')
            print('\nCASE '+name+' | h1 '+command,flush=True)
            print(self.net.get('h1').cmd(command),flush=True)
            received={}
            for host,path,ready,proc in processes:
                out,_=proc.communicate(timeout=15)
                assert proc.returncode==0,out.decode()
                received[host]=json.loads(path.read_text())
            actual=[h for h,packets in received.items() if packets]
            assert actual==([expected] if expected else []),(name,actual,expected)
            if expected:
                pkt=received[expected][0]
                assert pkt['ip_dst']==ip
                assert pkt['tunnel_dst']==dst
                if dst is not None: assert pkt['ttl']==64
            result={'case':name,'ip_destination':ip,'tunnel_destination':dst,'expected_receiver':expected,'actual_receivers':actual,'passed':True,'packets':received}
            results.append(result)
            print('PASS '+name+': received by '+str(actual),flush=True)
        (evidence/'tunnel-cases.json').write_text(json.dumps(results,indent=2))

topology='pod-topo/topology.json' if exercise=='basic' else 'topology.json'
runner=CheckedRunner(topology,'logs','pcaps',f'build/{exercise}.json','simple_switch_grpc')
try:
    runner.run_exercise()
except BaseException:
    if hasattr(runner,'net'):
        try: runner.net.stop()
        except Exception: pass
    raise
print('\nALL CHECKS PASSED: '+prefix,flush=True)
