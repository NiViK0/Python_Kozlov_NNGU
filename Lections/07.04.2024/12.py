import json
class TestEncoder(json.JSONEncoder):
   def default(self, o):
    return {"TITLE": o.title, "BODY": o.body, "CLASSNAME":o.__class__.__name__} #Test


class Test:
  def __init__(self, title, body):
    self.title = title
    self.body = body
# создаем экземпляр класса
t = Test("Some string", "Here is a bit more text, but still isn't enough")
qqq=json.dumps(t, cls=TestEncoder)
print("format json")
print(qqq)
dict=json.loads(qqq)
print(type(dict))
print(dict)

#{
# "TITLE":"Some string", 
# "BODY":"Here is a bit more text, but still isn't enough"
# "CLASSNAME":"Test"
#}
t_new=Test(dict["TITLE"],dict["BODY"]) #t_new   ("Some string","Here is a bit more text, but still isn't enough")
print("t_new")
print("t_new.title ",t_new.title)
print("t_new.body ",t_new.body)