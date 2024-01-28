f = open('/Users/nikitakozlov/Documents/Python_Kozlov_NNGU/Lections/28.01.2024/example2.txt', 'r+')

a=f.read()
f.write('\ninterface FastEthernet0/1\n  no shutdown\n  ip address 201.201.201.1 255.255.255.0')
print(f.closed)
f.close()
print(f.closed)

f = open('/Users/nikitakozlov/Documents/Python_Kozlov_NNGU/Lections/28.01.2024/example2.txt', 'r+')
a=f.read()
print(a)