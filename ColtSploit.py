import os
import sys
def logo():
  print("""                   
   ___________              __       _____________ ___________    __________              _____________ _____________   ________________
  |  _________|  __________| |      |_____  ______|  _________|  |         || |          |  _______   |      | |       |_______   ______|
  | |           |  ______  | |           | |      | |            | |    |  || |          | |       |  |      | |               | |
  | |           | |      | | |           | |      | |___________ | |_______|| |          | |       |  |      | |               | |
  | |           | |      | | |           | |      |___________  || |        | |          | |       |  |      | |               | |
  | |           | |      | | |           | |                  | || |        | |          | |       |  |      | |               | |
  | |           | |      | | |           | |                  | || |        | |          | |       |  |      | |               | |
  | |__________ | |______| | |_________  | |       ___________| || |        | |_________ | |_______|  |      | |               | |
  |____________||__________|___________|_|_|      |_____________||_|        |___________||____________| _____|_|_____          |_|
                           
                               ~ Changing Coder Name Won't Make Your One:)
                                  ~ The Dutchman 3xPloiTer:)
   """)
  

def help():
 print("""
  1="Port Scanner"
  2="Denial Of Service"
  3="MAC Spoofing.[must be root]"
  4="ARP Poisoning.[must be root]"
  5="Sniffing.[msut be root]"
  Choose attack you want to run by set his number in console\n""")
while True:
  cmd=raw_input("[*]ColtSploit@Console:~#").lower()
  if cmd=="help":
     help()
  elif "clear" in cmd:
     logo()
  elif "1" in cmd:
    os.system("python port_scanner.py")
  elif "2" in cmd:
    os.system("python dos.py")
  elif "3" in cmd:
    os.system("python MAC_spoofing.py")
  elif "4" in cmd:
    os.system("python arp_spoofer.py")
  elif "5" in cmd:
    os.system("python sniffer.py")
  elif "quit" in cmd:
    sys.exit()
