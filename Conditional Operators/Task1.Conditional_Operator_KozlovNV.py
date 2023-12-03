# Task_1
# Напишите программу, которая запрашивает у пользователя три числа в диапазоне 1-1000. Компьютер генерирует два случайных числа в диапазоне 1-100, 
# которые определяют отрезок. Определить какие  числа указанные пользователям попали в отрезок.

import random

A = random.randint(1,1000)
B = random.randint(1,1000) 

print("The computer guessed the beginning of the segment (A) and the end of the segment (B):")
print(A, "Point A")
print(B, "Point B")

Num_1 = int(input("Enter the first number in the range from 1 to 1000:"))
Num_2 = int(input("Enter the second number in the range from 1 to 1000:"))
Num_3 = int(input("Enter the third number in the range from 1 to 1000:"))

if Num_1 not in range(A) and (B):
    print("First number NOT in segment! Try it again!")
else:
    print("First number in segment!")
if Num_2 not in range(A) and (B):
    print("First number NOT in segment! Try it again!")
else:
    print("First number in segment!")
if Num_3 not in range(A) and (B):
    print("First number NOT in segment! Try it again!")
else:
    print("First number in segment!")