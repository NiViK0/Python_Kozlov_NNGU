import ipaddress
subnet1 = ipaddress.ip_network('80.0.1.0/28')
print(subnet1.broadcast_address)
print(subnet1.with_netmask)
print(subnet1.with_hostmask)
print(subnet1.prefixlen)
print(subnet1.num_addresses)
print(list(subnet1.subnets()))