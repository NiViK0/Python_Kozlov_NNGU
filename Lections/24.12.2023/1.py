class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age

    def _display(self): #private
        print(self.name)
        print(self.__age)

    def getAge(self):
        print(self.__age)

    def setAge(self, age):
        self.__age = age

person = Person('Dev', 30)
person.age=-31
person.display()
person.setAge(35)
person.getAge()
print("person.age ",person.age)