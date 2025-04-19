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
        self.employees = [] #database for all employee
    
    def add_employee(self, name, email, phone, address, age, designation, salary):
        employee =Employee(name, email, phone, address, age, designation, salary)
        self.employees.append(employee)
        print(f"{name} is added as a employee")

    def view_employee(self):
        print("----> Employee List <-----")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)

ad =Admin("admin", "admin@me.com", 21121, "dhaka")
ad.add_employee("e1", "e1@me.com", 322323, "lalbag", 27, "head-chef", 55353533)
ad.view_employee()


