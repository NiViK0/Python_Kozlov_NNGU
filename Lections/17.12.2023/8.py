
class DeskTable:
    
    def __init__(self):
        self.length=int(input("Введите длину стола"))
        self.width=int(input("Введите ширину стола"))
        self.high=int(input("Введите высота стола"))
        self.color=input("Введите цвет стола")
        self.current_s=self.length*self.width
        self.list=[]
        
    def Print(self):
        print("Длина стола",self.length)
        print("Ширина стола",self.width)
        print("высота стола",self.high)
        print("цвет стола",self.color)
        print("Список вещей на столе",self.list)
    
    def CountS(self):
       return (self.length*self.width)
    #-	создайте метод изменения длины прямоугольника с проверкой на положительное значение и с проверкой на число (вводить буквы - нельзя)
    def SetColor(self,color_new):
        self.color=color_new
    def SetLength(self,length_new):
       if isinstance(length_new, int)and (length_new>0)and(length_new>=self.width):
           self.length=length_new
       else:
            print("операция не может быть выполнена из-за ввода недопустимых значений")
    def AddItem(self, name, s1):
        if ( self.current_s >= s1):
            self.list.append(name)
            self.current_s = self.current_s-s1
        else:
            print("объект ", name, " разместить на столе нельзя")
#-------------main----------
a=DeskTable()
a.Print()
color_new=input("Введите цвет стола")
a.SetColor(color_new)
length_new=input("Введите новую длину стола")
a.SetLength(length_new)
a.Print()

def remove_object_from_table(AddItem):
    new_list = list_of_objects.copy()
    if object_to_remove in new_list:
        new_list.remove(object_to_remove)
    return new_list

result_list = remove_object_from_list(2)
print(result_list)  # вывод: [1, 3, 4, 5]