import re
line = '<text line> some text>'
match = re.search(r'<.*>', line)
print(match.group())

line = '1500 aab1.a1a1.a5d3 FastEthernet0/1'
print(re.search(r'\d+\s+\S+', line).group())

print(re.search(r'\d+\s+\S+?', line).group())

line = "FastEthernet0/1 10.0.12.1 YES manual up up"
match = re.search(r'(\S+)\s+([\w.]+)\s+.*', line)

print(match.group(0))
print(match.group(1))
print(match.group(2))

line1 = "FastEthernet0/1 10.0.12.1 YES manual up up"
match1 = re.search(r'(?P<intf>\S+)\s+(?P<address>[\d.]+)\s+', line1)
print(match1.group('intf'))
print(match1.group('address'))