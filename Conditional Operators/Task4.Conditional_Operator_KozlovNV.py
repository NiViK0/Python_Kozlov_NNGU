# Напишите программу, которая определяет пройдет коробка с размерами a*b*c в ящик с размерами x*y*z

a = int(input('Enter box height": a ='))
b = int(input('Enter the width of the box: b ='))
c =int(input('Enter box length: c ='))

x = int(input('Enter case height": x ='))
y = int(input('Enter the width of the case: y ='))
z =int(input('Enter case length: z ='))

if ((a == x and b == y and c == z) or
        (a == x and b == z and c == y) or
        (a == z and b == x and c == y) or
        (a == y and b == x and c == z) or
        (a == y and b == z and c == x) or
        (a == z and b == y and c == x)):
    print('Boxes and case are equal')
elif ((a <= x and b <= y and c <= z) or
        (a <= x and b <= z and c <= y) or
        (a <= z and b <= x and c <= y) or
        (a <= y and b <= x and c <= z) or
        (a <= y and b <= z and c <= x) or
        (a <= z and b <= y and c <= x)):
    print('The box is smaller than the case')
elif ((a >= x and b >= y and c >= z) or
        (a >= x and b >= z and c >= y) or
        (a >= z and b >= x and c >= y) or
        (a >= y and b >= x and c >= z) or
        (a >= y and b >= z and c >= x) or
        (a >= z and b >= y and c >= x)):
    print('The box is larger than the case')
else:
    print('Boxes and case are incomparable')
