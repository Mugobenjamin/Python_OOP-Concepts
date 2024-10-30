# class keyword to define a class(car)
class Car:

    def __init__(self, make, model, yom, color, speed):
        self.make = make
        self.model = model
        self.yom = yom
        self.color = color
        self.speed = speed

# method
    def print_name(self):
        print(f"This is the {self.make} {self.model}")

    def get_speed(self, distance):
        print(f"This is the {self.make} {self.model} {self.speed} {distance}")

##Create objects
car1 = Car("Toyota", "Corolla", "2021", "Black", "240")
car2 = Car("Toyota","Camry","2010","Silver","120")

#to call method from class use the '.' syntax
car1.print_name()
car1.get_speed("Km/h")
car2.print_name()
car2.get_speed("Km/h")

