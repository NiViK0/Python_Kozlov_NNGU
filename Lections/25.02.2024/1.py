import re

int_line = ' MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec,'
reg1="MTU"
reg2="BW"
reg3="DLY"
match = re.search(reg1, int_line)
print(match.group())
match = re.search(reg2, int_line)
print(match.group())
match = re.search(reg3, int_line)
print(match.group())
match = re.search(r'MTU', int_line)
print(match)