import re

line = '100 aab1.a1a1.a5d3 FastEthernet0/1'
print(re.search(r'a+', line).group())

line = '100 aab1.a1a1.a5d3 FastEthernet0/1'
print(re.findall(r'a+', line))#.group())

sh_ip_int_br = 'Ethernet0/1 192.168.200.1 YES NVRAM up up'
print(re.search(r'\d+\.\d+\.\d+\.\d+', sh_ip_int_br).group())

email1 = 'user1@gmail.com'
email2 = 'user2.test@gmail.com'
print(re.search(r'\w+\.*\w+@\w+\.\w+', email1).group())
print(re.search(r'\w+\.*\w+@\w+\.\w+', email2).group())

mail_log = ['Jun 18 14:10:35 client-ip=154.10.180.10 from=user1@gmail.com, size=551', 'Jun 18 14:11:05 client-ip=150.10.180.10 from=user2.test@gmail.com, size=768']
for message in mail_log:
    match = re.search(r'\w+\.?\w+@\w+\.\w+', message)
    if match:
       print("Found email: ", match.group())