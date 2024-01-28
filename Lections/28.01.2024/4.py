with open('/Users/nikitakozlov/Documents/Python_Kozlov_NNGU/Lections/28.01.2024/example4.txt') as f:
        for line in f:
            if 'line protocol' in line:
                interface = line.split()[0]
            elif 'MTU is' in line:
                mtu = line.split()[-2]
                print('{:15}{}'.format(interface, mtu))