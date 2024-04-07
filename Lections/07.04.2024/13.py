import json
class Figure:
  def __init__(self, title, form, color):
    self.title = title
    self.form = form
    self.color = color
  def __str__(self):
    return f"Figure: {self.title}, {repr(self.form)}, {repr(self.color)}"
class Form:
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    return f"<Form: {self.name}>"
class Color:
  def __init__(self, name):
    self.name = name 
  def __repr__(self):
    return f"<Color: {self.name}>"
class JSONDataAdapter:
  @staticmethod
  def to_json(o):
    if isinstance(o, Figure):
      return json.dumps({
        "title": o.title,
        "form": o.form.name,
        "color": o.color.name,
      })
  @staticmethod
  def from_json(o):
    o = json.loads(o)
    try:
      form = Form(o["form"])
      color = Color(o["color"])
      figure = Figure(o["title"], form, color)
      return figure
    except AttributeError: print("Неверная структура")
if __name__ == '__main__':
# создадим несколько цветов
  black = Color("Black")
  yellow = Color("Yellow")
  green = Color("Green")
# несколько форм
  rountt = Form("Rounded")
  square = Form("Squared")
# объекты фигур
  figure_one = Figure("Black Square", form=square, color=black)
  figure_two = Figure("Yellow Circle", form=rountt, color=yellow)
  print("Отображение объектов")
  print(figure_one)
  print(figure_two)
  print()
# преобразуем данные в JSON
  jone = JSONDataAdapter.to_json (figure_one)
jone = JSONDataAdapter.to_json(figure_one)
jtwo = JSONDataAdapter.to_json(figure_two)
print("Отображение JSON")
print(jone)
print(jtwo)
print()
# восстановим объекты
  restored_one = JSONDataAdapter.from_json(jone)
  restored_two = JSONDataAdapter.from_json(jtwo)
  print("Отображение восстановленных объектов")
  print(restored_one)
  print(restored_two)