import json

dictData_1 = [[1,2],3,[4,55]]
print(type(dictData_1))
print(dictData_1)
jsonData_1 = json.dumps(dictData_1)
print("jsonData_1")
print(jsonData_1)

with open("data.json", "w") as file:
  file.write(jsonData_1)
  
with open('data.json', 'r') as j:
  json_data_p = json.load(j)

print(json_data_p)
print(type(json_data_p))