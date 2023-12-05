#Написать программу: дан список из 10 чисел, которые задаются с помощью датчика случайных чисел. 
#Программа находит повторяющиеся элементы и считает количество повторений. 
#Например дан список (1,1,1,2,3,4,2,3,4) результат число 1 повторяется 3 раза, число 2 – 2раза, число 3 - 2 раза, число 4 – 2 раза   

from random import randint


def duplicate_count(numbers):
    duplicate_count = {}
    for number in numbers:
        duplicate_count[number] = duplicate_count.get(number, 0) + 1
    return duplicate_count


numbers = [randint(1, 10) for _ in range(10)]
duplicate_count_dict = duplicate_count(numbers)
for number, count in duplicate_count_dict.items():
    print(f"{number} повторяется {count} раз(а)")
print(numbers)