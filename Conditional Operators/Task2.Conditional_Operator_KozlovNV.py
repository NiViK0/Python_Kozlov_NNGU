#Task2
# Напишите программу, которая у пользователя запрашивает два числа. +
# Находит произведение чисел, если оба числа четные. +
# Находит сумму двух чисел если оба числа нечетные. + 
# Находит максимум из двух чисел если одно число нечетное, а другое четное. 
# Находит деление двух чисел, если одно число является делителем второго числа. 
# Результат вывести на экран

Num_1 = int(input("Enter the first number:"))
Num_2 = int(input("Enter the second number:"))

if Num_1 % 2 == 0 and Num_2 % 2 == 0:
    print(f"{Num_1},{Num_2} Both numbers are even. One number is a divisor of another. \n Enter "*" if you need to find the result of a multiplication:")
    A = int(input "Enter "*" if you need to find the result of a multiplication:")
    if A == 1:
        Num_3 = Num_1 * Num_2
    elif A == 2: 
        Num_3 = Num_1 // Num_2
    
    print((f'{Num_3}'))

elif Num_1 % 2 !=0 and Num_2 % 2 != 0 :
    Num_3 = Num_1 + Num_2 
    print(f"Entered numbers are odd. Numbers should to be added {Num_1} and {Num_2}. Their sum will be equal to: {Num_3}")

elif Num_1 % 2 !=0 and Num_2 % 2 == 0:
    Num_3 = max(Num_1, Num_2) 
    print(f"Entered number {Num_1} is odd, {Num_2} - is even number, Finding the maximum of number {Num_3}")

elif Num_2 % 2 != 0 and Num_1 % 2 == 0:
    Num_3 = max(Num_1, Num_2)
    print(f"Entered number {Num_2} is odd, {Num_1} - is even number, Finding the maximum of number {Num_3}")

elif Num_1 % Num_2 == 0:
    Num_3 = Num_1 // Num_2 
    print(f"{Num_1} is divided by {Num_2}, Finding the result of divide {Num_3}")