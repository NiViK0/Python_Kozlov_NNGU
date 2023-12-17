class Rectangle:
    def __init__(self):
        self.length=int(input("Введите длину прямоугольника"))
        self.width=int(input("Введите ширину прямоугольника"))
        
    def Print(self):
        print("Длина прямоугольника",self.length)
        print("Ширина прямоугольника",self.width)
    
    def CountP(self):
       return (self.length+self.width)*2
    def CountS(self):
       return (self.length*self.width)
    
    def SetLength(self,length_new):
       if isinstance(length_new, int):
           self.length=length_new
       else:
            print("операция не может быть выполнена из-за ввода недопустимых значений")
#-------------main----------
a=Rectangle()
a.Print()
print("Периметр прямоугольника ", a.CountP())
a.SetLength(13)
a.Print()