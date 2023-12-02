#Task 5
#Напишите программу, которая у пользователя запрашивает одно число. Находит делители данного числа от 2 до 10 и выводит на экран найденные делители

A = int(input("Enter the number:"))

Devisor = []

for i in range(2, 11):
    if A % i == 0:
        Devisor.append(i)

if Devisor:
    print(f"Number divisors {A} (from 2 to 10) re the numbers: {Devisor}")
else:
    print*(f"The number {A} has no divisors from 2 to 10.")