import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear',shell=True)
rhost=str(raw_input("Enter the remote ip adress:"))
p1=int(raw_input("Enter the start port number:"))
p2=int(raw_input("Enter the last port number:"))
print"*"*50
print"\n The Dutchman scanner is working on",rhost
print"*"*50
t1=datetime.now()
try:
  for port in range(p1,p2):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result=sock.connect_ex((rhost,port))
    if result==0:
       print"port open:-->\t",port
    sock.close()
except KeyboardInterrupt:
    print"you stop this"
    sys.exit()
except socket.gaierror:
    print"Hostname could not be resolved"
    sys.exit()
except socket.error:
    print"could not connect to server"
    sys.exit()
t2=datetime.now()
total=t2-t1
print"Scanning complete in",total