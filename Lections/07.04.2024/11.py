import json
class TestEncoder(json.JSONEncoder):
   def default(self, o):
    return {"TITLE": o.title, "BODY": o.body, "CLASSNAME":o.__class__.__name__}


class Test:
  def __init__(self, title, body):
    self.title = title
    self.body = body
# создаем экземпляр класса
t = Test("Some string", "Here is a bit more text, but still isn't enough")
qqq=json.dumps(t, cls=TestEncoder)
print("format json")
print(qqq)