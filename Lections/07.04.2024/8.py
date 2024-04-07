class Test:
  def __init__(self, title, body):
    self.title = title
    self.body = body...
# создаем экземпляр класса
t = Test("Some string", "Here is a bit more text, but still isn't enough")
# пытаемся сериализовать его в JSON, но...
json.dumps(t)
class Test:
  def __init__(self, title, body):
    self.title = title
    self.body = body
# создаем экземпляр класса
t = Test("Some string", "Here is a bit more text, but still isn't enough")
# пытаемся сериализовать его в JSON, но...
json.dumps(t)