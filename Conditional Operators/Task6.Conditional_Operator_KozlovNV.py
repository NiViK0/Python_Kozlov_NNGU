# Напишите программу, которая у пользователя запрашивает три числа  определяющие стороны треугольника. 
# Определить тип треугольника:  равнобедренный, равносторонний, прямоугольный, обычный

a = int(input('Enter first number":'))
b = int(input('Enter second number:'))
c = int(input('Enter third number'))

if a != b != c and a != c != b:
    print('Scalene triangle')
elif a == b == c:
    print('Equilateral triangle')
else:
    print('Isosceles triangle')