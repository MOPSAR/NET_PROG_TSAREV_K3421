# 2026-10-04 16:17:50 by RouterOS 7.23.7
# system id = wIm+sa2iVrA
#
/interface bridge add comment="Lab2 loopback" name=lo-lab protocol-mode=none
/interface ethernet set [ find default-name=ether1 ] disable-running-check=no
/interface ethernet set [ find default-name=ether2 ] disable-running-check=no
/interface ovpn-client add auth=sha256 certificate=chr2.crt_0 cipher=aes256-cbc connect-to=20.25.48.31 mac-address=FE:B1:31:93:4A:25 name=ovpn-azure use-peer-dns=no user=chr2 verify-server-certificate=yes
/routing ospf instance add disabled=no name=lab2 router-id=10.255.0.2
/routing ospf area add instance=lab2 name=backbone-lab2
/ip neighbor discovery-settings set discover-interface-list=none
/ip address add address=10.10.12.2/30 comment="Lab2 OSPF transit" interface=ether2 network=10.10.12.0
/ip address add address=10.255.0.2 comment="Lab2 Router ID" interface=lo-lab network=10.255.0.2
/ip address add address=172.20.30.2/24 comment="Lab3 NetBox managed" interface=ether2 network=172.20.30.0
/ip dhcp-client add interface=ether1 name=client1
/ip service set ftp disabled=yes
/ip service set telnet disabled=yes
/ip service set api disabled=yes
/ip service set api-ssl disabled=yes
/routing ospf interface-template add area=backbone-lab2 comment="Lab2 transit" interfaces=ether2 networks=10.10.12.0/30 type=ptp
/routing ospf interface-template add area=backbone-lab2 comment="Lab2 loopback" interfaces=lo-lab networks=10.255.0.2/32 passive
/system identity set name=CHR2
/system ntp client set enabled=yes
/system ntp client servers add address=162.159.200.1
/system ntp client servers add address=162.159.200.123
