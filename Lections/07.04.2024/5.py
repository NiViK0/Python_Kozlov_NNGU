import json

dictData_1 = (210450,"admin","John Smith","root", 5550505,"smith@mail.com",True)
jsonData_1 = json.dumps(dictData_1)
print("jsonData_1")
print(jsonData_1)


with open("data.json", "w") as file:
  file.write(jsonData_1)