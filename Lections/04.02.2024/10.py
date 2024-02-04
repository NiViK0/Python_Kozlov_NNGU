import os
import shutil
# вывести текущую директорию
print("Текущая деректория:", os.getcwd())
os.mkdir("One")
print(os.listdir())
os.makedirs("Two/qqq1")
os.makedirs("Two/qqq2")
print(os.listdir())
print(os.listdir("./Two/"))
os.rmdir("Two/qqq2")
print(os.listdir("./Two/"))
text_file = open("./Two/qqq1/text.txt", "w")
text_file.write("Это текстовый файл")
print(os.listdir("./Two/qqq1"))
shutil.rmtree("Two/qqq1")
print(os.listdir("./Two/"))