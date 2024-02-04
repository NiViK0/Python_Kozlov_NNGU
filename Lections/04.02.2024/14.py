
import ipaddress
subnet1 = ipaddress.ip_network('192.168.1.0/24')
print(subnet1.broadcast_address)
print(subnet1.with_netmask)
print(subnet1.with_hostmask)
print(subnet1.prefixlen)
print(subnet1.num_addresses)
print(list(subnet1.subnets()))
for ip in subnet1:
  print(ip)
print("subnet1[10] ",subnet1[10])