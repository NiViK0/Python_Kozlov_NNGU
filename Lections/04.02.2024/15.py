import ipaddress
int1 = ipaddress.ip_interface('10.0.1.1/24')
print(int1.ip)
print(int1.network)
print(int1.netmask)

