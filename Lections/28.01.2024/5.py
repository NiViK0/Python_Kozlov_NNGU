with open('/Users/nikitakozlov/Documents/Python_Kozlov_NNGU/Lections/28.01.2024/example4.txt') as f:
 for line in f:
   if 'line protocol' in line:
    interface = line.split()[0]
   elif 'Internet address' in line:
    ip_address = line.split()[-1]
   elif 'MTU' in line:
    mtu = line.split()[-2]
    print('{:15}{:17}{}'.format(interface, ip_address, mtu))