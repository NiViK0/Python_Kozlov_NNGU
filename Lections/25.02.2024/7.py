import re 

cdp = '''
...: SW1#show cdp neighbors detail
...: -------------------------
...: Device ID: SW2
...: Entry address(es):
...: IP address: 10.1.1.2
...: Platform: cisco WS-C2960-8TC-L, Capabilities: Switch IGMP
...: Interface: GigabitEthernet1/0/16, Port ID (outgoing port): GigabitEthernet0/1
...: Holdtime : 164 sec
...: '''
print(re.search(r'Interface.+Port ID.+', cdp).group()) 

line = "100 aa12.35fe.a5d3 FastEthernet0/1"
print(re.search(r'^\d+', line).group())

line = "100 aa12.35fe.a5d3 FastEthernet0/1"
print(re.search(r'^\d+', line).group())
print(re.search(r'\d+$', line).group())


line = "100 aa12.35fe.a5d3 FastEthernet0/1"
print(re.search(r'^\d+', line).group())
print(re.search(r'\d+\/\d+$', line).group())


line = "100 aa12.35fe.a5d3 FastEthernet0/1"
print(re.search(r'[0-9]+', line).group())

line = "100 aa12.35fe.a5d3 FastEthernet0/1"
print(re.search(r'[0-9]+', line).group())
print(re.search(r'^[0-9]+', line).group())
print(re.search(r'^[0-9]{1,4}', line).group())