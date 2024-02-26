import re
regex = r'(?P<mac>\S+) +(?P<ip>\S+) +\d+ +\S+ +(?P<vlan>\d+) +(?P<port>\S+)'
result = []
with open('/Users/nikitakozlov/Documents/Python_Kozlov_NNGU/Lections/25.02.2024/dhcp_snooping.txt') as data:
  for line in data:
    match = re.search(regex, line)
    if match:
      result.append(match.groupdict())
print('К коммутатору подключено {} устройства'.format(len(result)))
for num, comp in enumerate(result, 1):
    print('Параметры устройства {}:'.format(num))
    for key in comp:
     print('{:10}: {:10}'.format(key, comp[key]))