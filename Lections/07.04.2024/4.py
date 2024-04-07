import json
#  data write  - - >> save json
#  file json - - >> read 
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
#list, tuple, set
#Car
  
jsonData_1 = json.dumps(dictData_1)
jsonData_2 = json.dump

print("jsonData_1")
print(jsonData_1)
print("jsonData_2")
print(jsonData_2)