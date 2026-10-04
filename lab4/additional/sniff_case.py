import sys,json,time
from pathlib import Path
sys.path.insert(0,'/tutorials/exercises/basic_tunnel')
from myTunnel_header import MyTunnel
from scapy.all import AsyncSniffer,IP,Raw,wrpcap
out,ready,marker=map(str,sys.argv[1:])
sniffer=AsyncSniffer(iface='eth0',store=True,started_callback=lambda:Path(ready).touch(),lfilter=lambda p: Raw in p and marker.encode() in bytes(p[Raw]))
sniffer.start()
time.sleep(5)
packets=sniffer.stop()
result=[{'ip_dst':p[IP].dst,'ttl':p[IP].ttl,'tunnel_dst':p[MyTunnel].dst_id if MyTunnel in p else None,'payload':bytes(p[Raw]).decode(errors='replace')} for p in packets]
Path(out).write_text(json.dumps(result,indent=2))
if packets: wrpcap(out.replace('.json','.pcap'),packets)
