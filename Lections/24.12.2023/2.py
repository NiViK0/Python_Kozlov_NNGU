import random

class MyList:
    def __init__(self):
        self.__spisok=[]
        
    def __add__(self,other):
        temp=MyList()
        if len(self.__spisok)>0 and len(self.__spisok)==len(other.__spisok):
           for i in range(len(self.__spisok)):
               temp.__spisok.append(self.__spisok[i]+other.__spisok[i])
           return temp
        else:
            print("сложение не возможно")
    
    def RemoveItem(self):
        if len(self.__spisok)>0:
          value=int(input("введите число для удаления "))
          p=self.__spisok.count(value)
          if p>0 :
             for i in range(p):
               self.__spisok.remove(value)
          else:
            print("удаление невозможно, заданное число в списке отсуствует")
        else:
          print("список пустой")
          
    def AddItem(self):
        value=int(input("введите число \n "))
        self.__spisok.append(value)
        
    def PrintSpisok(self):
        if len(self.__spisok)>0:
          print(self.__spisok)
        else:
          print("список пустой")
    
    def RandomInput(self):
        n=random.randint(1,20)
        for i in range(n):
            self.__spisok.append(random.randint(1,100))
        
    def ManualInput(self):
        n=int(input("введите количество чисел "))
        for i in range(n):
            value=int(input("введите число \n "))
            self.__spisok.append(value)
            #self.__spisok.append(int(input("введите число \n ")))

#-------------main---------
a=MyList()
b=MyList()
a.RandomInput()
b.RandomInput()
a.PrintSpisok()
b.PrintSpisok()
#d=MyList()
d=a+b
d.PrintSpisok()