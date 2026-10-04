# Р¤Р°Р№Р»С‹ Р»Р°Р±РѕСЂР°С‚РѕСЂРЅРѕР№ СЂР°Р±РѕС‚С‹ в„–4

РћСЃРЅРѕРІРЅРѕР№ РґРѕРєСѓРјРµРЅС‚: [РѕС‚С‡С‘С‚](../lab4_report.md). Рљ РЅРµРјСѓ РїСЂРёР»Р°РіР°СЋС‚СЃСЏ РґРІРµ РїСЂРѕРіСЂР°РјРјС‹ P4 Рё С„Р°Р№Р» СЃС…РµРј topologies.drawio.

РћСЃС‚Р°Р»СЊРЅС‹Рµ С„Р°Р№Р»С‹ РЅСѓР¶РЅС‹ РґР»СЏ РїРѕРІС‚РѕСЂРЅРѕРіРѕ Р·Р°РїСѓСЃРєР°: Dockerfile РѕРїРёСЃС‹РІР°РµС‚ СЃСЂРµРґСѓ, run_checks.py РІС‹РїРѕР»РЅСЏРµС‚ РїСЂРѕРІРµСЂРєРё РІ Mininet, sniff_case.py СЃРѕР±РёСЂР°РµС‚ РїР°РєРµС‚С‹, Р° JSON-С„Р°Р№Р»С‹ Р·Р°РґР°СЋС‚ С‚РѕРїРѕР»РѕРіРёРё Рё Р·Р°РїРёСЃРё С‚Р°Р±Р»РёС† РєРѕРјРјСѓС‚Р°С‚РѕСЂРѕРІ. РљР°С‚Р°Р»РѕРі evidence СЃРѕРґРµСЂР¶РёС‚ Р¶СѓСЂРЅР°Р»С‹ Рё СЂРµР·СѓР»СЊС‚Р°С‚С‹ Р·Р°С…РІР°С‚Р°.

## РџРѕРІС‚РѕСЂРЅС‹Р№ Р·Р°РїСѓСЃРє РІ РїРѕРґРіРѕС‚РѕРІР»РµРЅРЅРѕР№ Ubuntu

```bash
cd /home/labuser
sudo docker start netprog-p4-lab4
bash lab4/additional/run-lab.sh
```

РџСЂРё РїРµСЂРІРёС‡РЅРѕРј СЃРѕР·РґР°РЅРёРё:

```bash
git clone https://github.com/p4lang/tutorials.git p4-tutorials
git -C p4-tutorials checkout 098ce0b7ae486f5b747a6b53ad1585f0d977b42e
sudo docker build -t netprog-p4-lab4 lab4/additional/additional
cp lab4/basic.p4 p4-tutorials/exercises/basic/basic.p4
cp lab4/basic_tunnel.p4 p4-tutorials/exercises/basic_tunnel/basic_tunnel.p4
sudo docker run -d --name netprog-p4-lab4 --privileged \
  -v /home/labuser/p4-tutorials:/tutorials \
  -v /home/labuser/lab4:/lab netprog-p4-lab4 sleep infinity
```

Р—Р°РїСѓСЃРє `make test` upstream РїСЂРѕРІРµСЂСЏРµС‚ СЌС‚Р°Р»РѕРЅ РёР· `solution/`; РґР»СЏ РїРѕРґС‚РІРµСЂР¶РґРµРЅРёСЏ РёРјРµРЅРЅРѕ РїСЂРёР»РѕР¶РµРЅРЅС‹С… `.p4` РёСЃРїРѕР»СЊР·СѓРµС‚СЃСЏ `make build` Рё `run_checks.py` РЅР° РѕСЃРЅРѕРІРЅРѕР№ РїСЂРѕРіСЂР°РјРјРµ СѓРїСЂР°Р¶РЅРµРЅРёСЏ.
