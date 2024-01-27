#Дан список некоторых целых чисел, найдите значение 20 в нем и, если оно присутствует, замените его на 200. 
# Обновите список только при первом вхождении числа 20.
# Поменять местами самый большой и самый маленький элементы списка

from random import randint

# Work method to finde and change exclude number
numbers = [randint(0, 20) for i in range(20)]
print('The list before change:', numbers)

max_number = max(numbers)
print(max_number)
min_number = min(numbers)
print(min_number) 

numbers[numbers.index(max_number)] = min_number
numbers[numbers.index(min_number)] = max_number
print('The list after changes:', numbers)

