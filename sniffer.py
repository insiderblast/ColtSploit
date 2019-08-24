import socket
import struct
import binascii
import os
interface=str(raw_input("Enter Interface name you want to bind:"))
os.system("ifconfig "+interface+" promisc")
s=socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.ntohs(0x0800))
while True:
  pkt=s.recvfrom(2048)
  eth_head=pkt[0][0:14]
  eth=struct.unpack("!6s6s2s",eth_head)
  print"--------Ethernet Frame----------------------"
  print"Destination MAC ",binascii.hexlify(eth[0])
  print" Source MAC",binascii.hexlify(eth[1])
  binascii.hexlify(eth[2])
  ipheader=pkt[0][14:34]
  ip_hdr=struct.unpack("!12s4s4s",ipheader)
  print"--------IP-----------------------------------"
  print"Source IP",socket.inet_ntoa(ip_hdr[1])
  print"Destination IP",socket.inet_ntoa(ip_hdr[2])
  print"--------TCP-----------------------------------"
  tcpheader=pkt[0][34:54]
  #tcp_hdr=struct.unpack("!HH16s",tcpheader)
  tcp_hdr=struct.unpack("HH9ss6s",tcpheader)
  print"Source port",tcp_hdr[1]
  print"Flag",binascii.hexlify(tcp_hdr[3])