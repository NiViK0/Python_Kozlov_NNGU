#Написать программу – игра - угадай, в которой с помощью функции random генерируется случайное число от 1 до 50. 
#Пользователю предлагается угадать данное число, на основе подсказать – загаданное число больше или меньше числа пользователя. 
#Вывести число попыток отгадывания числа

from random import randint

number_1 = int(input("Print first number"))
number_2 = int(input("Print second number"))

if number_2 < number_1:
    number_1, number_2 = number_2,number_1

k3 = 0
k5 = 0
k9 = 0 

for iter in range (number_2):
    if iter % 3 == 0: 
        k3 = k3 + 1
    if iter % 5 == 0:
        k5 = k5 + 1
    if iter % 9 == 0:
        k9 = k9 + 1
        
print("k3",k3," k5 ",k5,"k9",k9)



