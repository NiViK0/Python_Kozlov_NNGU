#Задача 5. Сжатие списка - дан список целых чисел. Требуется “сжать” его, переместив все ненулевые элементы в левую часть списка,
#не меняя их порядок, а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя, дополнительный список 
#использовать нельзя, задачу нужно выполнить за один проход по списку. Распечатайте полученный список.
#Входные данные
#Вводится список чисел. Все числа списка находятся на одной строке.
#Выходные данные
#Выведите ответ на задачу.
#Примеры
#входные данные
#4 0 5 0 3 0 0 5
#выходные данные
#4 5 3 5 0 0 0 0 

input_list = list(map(int, input("List-compression.Input some numbers in list:").split()))
z_elem = len(input_list) - 1

for i in range(len(input_list)):
    if input_list[i] == 0:
        while z_elem > i:
            if input_list[z_elem] == 0:
                z_elem -= 1
            else: 
                input_list[i], input_list[z_elem] = input_list[z_elem], input_list[i]
                z_elem -= 1
                break
        else:
            break
print("Final result of list-compression:", input_list)