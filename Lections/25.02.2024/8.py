import re

line = "100 aa12.35fe.a5d3 FastEthernet0/1"
print(re.search(r'[a-f0-9]+\.[a-f0-9]+\.[a-f0-9]+', line).group())

line = "100 aa12.35fe.a5d3 FastEthernet0/1"
print(re.search(r'[a-f0-9]+[./][a-f0-9]+', line).group())

ine = 'FastEthernet0/0 15.0.15.1 YES manual up up'
print(re.search(r'[^a-zA-Z]+', line).group())

line = "100 aa12.35fe.a5d3 FastEthernet0/1"
print(re.search(r'[0-9]([a-f]|[0-9])[0-9]', line).group())

line1 = 'FastEthernet0/0 15.0.15.1 YES manual up up'
print(re.search(r'([0-9]+\.)+[0-9]+', line1).group())