import os
mac=str(raw_input("Enter the new MAC adress:"))
interface=str(raw_input("Enter your interface name:")) #Exemple wlan0 eth0 and other
os.system("ifconfig "+interface+" hw ether "+mac+" ")
os.system("ip link show "+interface+" ")
