#Написать программу: дан список из 10 чисел, которые задаются с помощью датчика случайных чисел в диапазоне 1-10.  
#Программа находит повторяющиеся элементы и удаляет их из списка. Например, дан список (1,1,1,2,3,4,2,3,4) результат (1,2,3,4)


from random import randint

def delete_duplicates(numbers):
    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers

numbers = [randint(1, 10) for i in range(10)]
result = delete_duplicates(numbers)
print(numbers)
print(result)