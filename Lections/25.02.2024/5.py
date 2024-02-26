
mac_table = '''
...: sw1#sh mac address-table
...: Mac Address Table
...: -------------------------------------------
...:
...: Vlan Mac Address Type Ports
...: ---- ----------- -------- -----
...: 100 a1b2.ac10.7000 DYNAMIC Gi0/1
...: 200 a0d4.cb20.7000 DYNAMIC Gi0/2
...: 300 acb4.cd30.7000 DYNAMIC Gi0/3
...: 1100 a2bb.ec40.7000 DYNAMIC Gi0/4
...: 500 aa4b.c550.7000 DYNAMIC Gi0/5
...: 1200 a1bb.1c60.7000 DYNAMIC Gi0/6
...: 1300 aa0b.cc70.7000 DYNAMIC Gi0/7
...: '''

for line in mac_table.split(
for line in mac_table.split('\n'):
  match = re.search(r'\d{1,4} +', line)
  if match:
    print('VLAN: ', match.group())