import random

# Создаем список из 10 случайных чисел
random_list = [random.randint(1, 10) for i in range(10)]

# Сортируем список
random_list.sort()

# Находим повторяющиеся элементы
duplicated_elements = []
for i in range(len(random_list)-1):
    if random_list[i] == random_list[i+1]:
        duplicated_elements.append(random_list[i])

# Удаляем найденные повторяющиеся элементы из списка
random_list = random_list[:len(random_list) - len(duplicated_elements)]

print("Список без повторяющихся элементов:", random_list)
print("Список повторяющихся элементов:", duplicated_elements)