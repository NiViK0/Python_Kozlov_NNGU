import json
dictData_1 = { 
   "ID" : 210450,
  "login" : "admin",
  "name" : "John Smith",
  "password" : "root",
  "phone" : 5550505,
  "email" : "smith@mail.com",
  "online" : True }
dictData_2 = { 
   "ID" : 222222,
  "login" : "admin",
  "name" : "Micle",
  "password" : "admin",
  "phone" : 5550505,
  "email" : "micle@goole.com",
  "online" : True }
jsonData_1 = json.dumps(dictData_1)
jsonData_2 = json.dumps(dictData_2)
print("jsonData_1")
print(jsonData_1)
print("jsonData_2")
print(jsonData_2)

with open("data.json", "w") as file:
  file.write(jsonData_1)
  file.write(jsonData_2)
  
with open('data.json', 'r') as j:
  json_data_p = json.load(j)

print(json_data_p)
print(type(json_data_p))