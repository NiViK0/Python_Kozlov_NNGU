class Car:
    # create class attributes
    car_count = 0
    # create class methods
    def start(self, name, make, model):
        print ("Engine started")
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1

#------------main ------------
car_a = Car()
car_a.start("Corrola", "Toyota", 2015)
print(car_a.name)
print(car_a.car_count)

car_b = Car()
car_b.start("City", "Honda", 2013)
print(car_b.name)
car_b.color="black"
print(car_b.color)
print(car_b.car_count)