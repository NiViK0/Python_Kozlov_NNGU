
result = {}
with open('/Users/nikitakozlov/Documents/Python_Kozlov_NNGU/Lections/28.01.2024/example3.txt') as f:
    for line in f:
        line_list = line.split()
        if line_list and line_list[1][0].isdigit():
            interface = line_list[0]
            address = line_list[1]
            result[interface] = address
print(result)