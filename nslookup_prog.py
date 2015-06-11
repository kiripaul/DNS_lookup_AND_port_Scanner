import subprocess as sbpr
import socket as sckt
import re

site = input("Enter Domain Name: ")


print('='*60+'\n'+'+'*18+" RESOLVING IP'S "+'+'*18)

out = sbpr.check_output(['nslookup',site],universal_newlines=True)

print(out)

##REGEX for finding IP addresses
ipAddresses = re.findall('[0-9]+(?:\.[0-9]+){3}',out)

print('='*60+'\n'+'+'*18+' SCANNING PORTS '+'+'*18)

gEnd = len(ipAddresses)

#Check which ports are open for each IP Address...this shit takes a while
for i in range(1,gEnd):
    ip = ipAddresses[i]
    iP = str(ip)
    print("-- IP ADDRESS --"+iP + ":\n")
    for port in range(1,1025):
        sock = sckt.socket(sckt.AF_INET, sckt.SOCK_STREAM)
        result = sock.connect_ex((iP,port))
        if result == 0:
            print("\t\tPort {}: Open".format(port))
        sock.close()
