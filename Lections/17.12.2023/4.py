class Car:
    # create class attributes
    car_count = 0
    # create class methods
    def __init__(self,make, color):   #  конструктор, предназначенный для инициализации обязательных атрибутов экзепмляра
        self.make = make
        self.color = color
        Car.car_count +=1
        print(Car.car_count)

    def start(self, name, model):
        print ("Engine started")  #car_a, car_b, car_d 
        self.name = name  # атрибут экземпляра
        #self.make = make  # атрибут экземпляра
        self.model = model  # атрибут экземпляра  1930-2023   -1993  1123
        #Car.car_count += 1
    def add_color(self, color):
        self.color = color  # атрибут экземпляра
    def PrintColor(self):
        print("color car ", self.color)
    def PrintC(number):
        #print("color car ", self.color)
        print("car_count ", Car.car_count)
        print("number ", number)
        
     
#------------main ------------
car_a = Car("Toyota","Orange") #  переменная класс, экземпляр класса, объект класса
car_a.PrintColor()

car_a.start("Corrola", 2015)
print(car_a.name)
car_a.add_color("white")
#print(car_a.color)   #car_a:  name, make,  model, color
car_a.PrintColor()
Car.PrintC(17)


car_b = Car("Honda","Black")
car_b.start("City", 2013)
print(car_b.name)    #car_b:  name, make,  model
car_b.PrintColor()

print(Car.car_count)