class Car:

    # create class attributes
    name = "c200"
    make = "mercedez"
    model = 2008

    # create class methods
    def start(self):
        print ("Engine started")

    def stop(self):
        print ("Engine switched off")

# -------------main ----------------

car_a = Car()
car_b = Car()

print("car_a.make ",car_a.make)
print("car_b.make ",car_b.make)