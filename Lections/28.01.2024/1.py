
f = open('/Users/nikitakozlov/Documents/Python_Kozlov_NNGU/Lections/28.01.2024/example2.txt', 'r')

#print(f.read(7))
#print(f.read(10))

#a=f.readline()
#print(a)

list_config = []
for line in f:   #чтение построчно 
    list_config.append(line)
    
    print(list_config)

#a=f.read()
#print(a)

#b=f.read()
#print(b)
#print(*f)