#Написать программу: дан список из 10 чисел, которые задаются с помощью датчика случайных чисел в диапазоне 1-10.  
#Программа находит повторяющиеся элементы и удаляет их из списка. 
#Например, дан список (1,1,1,2,3,4,2,3,4) результат (1,2,3,4)


import random 

# Функция для удаления повторяющихся элементов из списка 
def removeDuplicates(lst): 
  result = [] 
  for num in lst: 
    if num not in result: 
      result.append(num) 
  return result 

# Генерация списка из 10 случайных чисел 
randomList = [random.randint(1, 10) for i in range(10)]  

# Вывод исходного списка 
print("Исходный список:", randomList) 

# Удаление повторяющихся элементов 
resultList = removeDuplicates(randomList) 

# Вывод списка без повторяющихся элементов
print("Результат:", resultList)