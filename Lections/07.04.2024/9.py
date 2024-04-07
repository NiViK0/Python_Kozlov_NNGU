import json
def to_json(obj):
  if isinstance(obj, Test):
    result = obj.__dict__
    result["className"] = obj.__class__.__name__
    return result

class Test:
  def __init__(self, title, body):
    self.title = title
    self.body = body
# создаем экземпляр класса
t = Test("Some string", "Here is a bit more text, but still isn't enough")
qqq=json.dumps(t, default=to_json)
print(qqq)