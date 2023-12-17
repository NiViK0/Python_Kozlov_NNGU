class Car:
    # create class attributes
    car_count = 0
    # create class methods
    def start(self, name, make, model):
        print ("Engine started")  #car_a, car_b, car_d 
        self.name = name  # атрибут экземпляра
        self.make = make  # атрибут экземпляра
        self.model = model  # атрибут экземпляра  1930-2023   -1993  1123
        Car.car_count += 1
    def add_color(self, color):
        self.color = color  # атрибут экземпляра
    def PrintColor(self):
        print("color car ", self.color)
    def PrintC(number):
        #print("color car ", self.color)
        print("car_count ", Car.car_count)
        print("number ", number)
        
     
#------------main ------------
car_a = Car() #  переменная класс, экземпляр класса, объект класса
car_a.start("Corrola", "Toyota", 2015)
print(car_a.name)
car_a.add_color("white")
#print(car_a.color)   #car_a:  name, make,  model, color
car_a.PrintColor()
#car_a.PrintC(17)
Car.PrintC(17)

car_b = Car()
car_b.start("City", "Honda", 2013)
print(car_b.name)    #car_b:  name, make,  model

#car_b.color="black"  # добавление атрибута экземпляра 
#print(car_b.color) 

#del car_b.color
#print(car_b.color)

print(Car.car_count)

