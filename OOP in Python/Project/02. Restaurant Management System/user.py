from abc import ABC

class User(ABC):
    def __init__(self, name, email, phone, address):
        self.name =name
        self.phone = phone
        self.email = email
        self.address = address


class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, email, phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary

# emp = Employee("me", "me@me.com", 121221, "dhaka", 25, "chef", 23232222)
# print(emp.name)

class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
    
    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)

    def view_employee(self, restaurant):
        restaurant.view_employee()

class Restaurant:
    def __init__(self, name):
        self.name= name
        self.employees = [] #database for all employee

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} is added as a employee")

    def view_employee(self):
        print("----> Employee List <-----")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)



class Menu:
    def __init__(self):
        self.items = [] # items ar database
    
    def add_menu_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("item deleted")
        else:
            print("item not found")

res = Restaurant('mamar hotel')
admin = Admin("admin", "admin@me.com", 21121, "dhaka")


e1 = Employee("e1", "e1@me.com", 322323, "lalbag", 27, "head-chef", 55353533)

admin.add_employee(res, e1)

admin.view_employee(res)


