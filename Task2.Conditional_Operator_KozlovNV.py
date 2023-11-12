#Task2
# Напишите программу, которая у пользователя запрашивает два числа. +
# Находит произведение чисел, если оба числа четные. +
# Находит сумму двух чисел если оба числа нечетные. + 
# Находит максимум из двух чисел если одно число нечетное, а другое четное. 
# Находит деление двух чисел, если одно число является делителем второго числа. 
# Результат вывести на экран

Num_1 = int(input("Enter the first number:"))
Num_2 = int(input("Enter the second number:"))

Multply = Num_1 * Num_2
Addition = Num_1 + Num_2

if Num_1 and Num_2 % 2 != 0:
    print(Addition,"The result of addition. The numbers are odd.")
else:
    print(Multply,"The result of multiplication, because the numbers are even.")