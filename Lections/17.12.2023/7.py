
class Writing_Table:   
    def __init__(self):
        self.length=int(input("Введите длину стола"))
        self.width=int(input("Введите ширину стола"))
        self.height=int(input("Введите высоту стола"))
        self.color=int(input("Введите цвет стола"))

    def print(self):
     print(f"Ширина: {self.width}, Высота: {self.height}, Длина: {self.length}, Цвет: {self.color}")

    def PrintS(Writing_Table):
        return Writing_Table.width * Writing_Table.height
      
    def __Check__(self):
        return (self.length*self.width)
    def SetColot(self, color_new):
       self.color=color_new
