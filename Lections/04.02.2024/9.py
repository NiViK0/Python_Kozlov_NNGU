import os
# вывести текущую директорию
print("Текущая деректория:", os.getcwd())
os.mkdir("One")
print(os.listdir())
os.makedirs("Two/qqq")
print(os.listdir())
print(os.listdir("./Two/"))