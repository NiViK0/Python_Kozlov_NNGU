import re

int_line = ' MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec,'


log2 = 'Oct 3 12:49:15.941: %SW_MATM-4-MACFLAP_NOTIF: Host f04d.a206.7fd6 in vlan 1 is flapping between port Gi0/5 and port Gi0/16'
print(re.search(r'Host (\S+) in vlan (\d+) is flapping between port (\S+) and port (\S+)', log2).groups())

log = '*Jul 7 06:15:18.695: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/3, changed state to down'
print(re.search(r'\d\d:\d\d:\d\d', log).group())

log2 = 'Jun 3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'
print(re.search(r'\w\w\w\w\.\w\w\w\w\.\w\w\w\w', log2).group())

line = '100 aab1.a1a1.a5d3 FastEthernet0/1'
print(re.search(r'a+', line).group())

line = '100 aab1.a1a1.a5d3 FastEthernet0/1'
print(re.findall(r'a+', line))#.group())