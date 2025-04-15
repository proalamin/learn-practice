# Composition means a class has objects of other classes inside it — like building something using smaller parts.

class Battery:
    def charge(self):
        print("Charging battery...")

class Phone:
    def __init__(self):
        self.battery = Battery()  # Composition
    
    def use(self):
        print("Using phone")
        self.battery.charge()

class SmartPhone(Phone):  # Inheritance
    def use(self):
        print("Using smart features")
        self.battery.charge()

p = SmartPhone()
p.use()
