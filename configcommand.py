from netmiko import ConnectHandler
import getpass
import sys
import time

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.10.10',
    'username': 'username',
    'password': 'password',
    'secret': 'password'
}
ipfile = open("iplist.txt")
print("Script for SSH to device, Please enter your credential")
device['username'] = input("User name ")
device['password'] = getpass.getpass()
device['secret'] = input("Enter enable password: ")
configfile = open("configfile.txt")
configset = configfile.read()
configfile.close()

for line in ipfile:
    device['ip'] = line.strip("\n")
    print("\n\nConnecting Device ", line)
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    time.sleep(2)
    print("Passing configuration set ")
    net_connect.send_config_set(configset)
    print("Device Conigured ")

ipfile.close()
