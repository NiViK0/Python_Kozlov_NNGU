#Сделать копию скрипта задания 1. Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
#• состоит из 4 чисел (а не букв или других символов)
#• числа разделенны точкой
#• каждое число в диапазоне от 0 до 255
#Если адрес задан неправильно, выводить сообщение: «Неправильный IP-адрес». Сообщение «Неправильный IP-адрес» должно выводиться только один раз, даже если несколько пунктов выше не выполнены.
#Ограничение: Все задания надо выполнять используя только пройденные темы.

#1
input_list = input('Print IP-address') #10.0.1.1.
for iter in input_list:
    if iter.isdigit() == False:
        print("IP-address is incorrect")
        
#2
if len(input_list)!=4:
    print("Error in input")    
    
#3 
for iter in input_list: 
    if iter.isdigit()== True and int(iter) > 255 and int(iter) < 0: 
        print("")