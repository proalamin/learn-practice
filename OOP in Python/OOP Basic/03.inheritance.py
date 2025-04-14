class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def speed(self):
        pass


class Car(Vehicle):   # inheritance
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

class ElectricCar(Car): # multi level inheritance
    def __init__(self, brand, model, capacity, battery_milage):
        super().__init__(brand, model, capacity)
        self.batter_life =battery_milage


class Bike(Vehicle):
    def __init__(self, brand, model, milage):
        super().__init__(brand, model)
        self.milage = milage

bmw = Car("BMW", "A8", 4)
# print(bmw.brand, bmw.model, bmw.capacity)

xiomi = ElectricCar('Xiomi', 'Xm1', 4, 900)
print(xiomi.brand)