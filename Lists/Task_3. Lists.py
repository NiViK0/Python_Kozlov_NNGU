#Дан список некоторых целых чисел, найдите значение 20 в нем и, если оно присутствует, замените его на 200. 
# Обновите список только при первом вхождении числа 20.

from random import randint

# Work method to finde and change exclude number
numbers = [randint(0, 20) for i in range(20)]
numbers[numbers.index(20)] = 200
print(numbers)

# Second method to find exclude number 
if numbers.count(20):
    print('Element found')
else:
    print('Element not found')
    
# Third method to find exclude number 
index = numbers.index(int(20))
print('Position of exclude number in list:', index)





