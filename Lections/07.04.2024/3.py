import json
#  data write  - - >> save json
#  file json - - >> read 
dictData = { 
   "ID" : 210450,
  "login" : "admin",
  "name" : "John Smith",
  "password" : "root",
  "phone" : 5550505,
  "email" : "smith@mail.com",
  "online" : True }
  
jsonData = json.dumps(dictData)
print(jsonData)

with open("data.json", "w") as file:
  file.write(jsonData)