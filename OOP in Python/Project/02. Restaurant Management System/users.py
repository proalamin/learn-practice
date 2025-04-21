from abc import ABC
from orders import Order

class User(ABC):
    def __init__(self, name, email, phone, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("item quantity not available right now")
            else:
                item.quantity=quantity
                self.cart.add_item(item)
                print(f"{item.name} added to cart")
        else:
            print("Item not found")

    def view_cart(self):
        print("-----> View Cart <------")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{item.quantity}")
        print(f"Total price: {self.cart.total_price}")
    
    def pay_bill(self):
        print(f"{self.cart.total_price} tk paid successfully")
        self.cart.clear()

class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, email, phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)

    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)

    def view_employee(self, restaurant):
        restaurant.view_employee()

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def del_item(self, restaurant, item_name):
        restaurant.menu.remove_item(item_name)


# # --- Usage Example ---
# res = Restaurant('Mamar Hotel')
# admin = Admin("admin", "admin@me.com", 21121, "dhaka")
# e1 = Employee("e1", "e1@me.com", 322323, "lalbag", 27, "head-chef", 55353533)

# admin.add_employee(res, e1)
# admin.view_employee(res)

# # Add menu items
# admin.add_new_item(res, FoodItem("pizza", 999, 50))
# admin.add_new_item(res, FoodItem("burger", 699, 80))
# admin.add_new_item(res, FoodItem("hot dog", 799, 30))

# # View menu
# admin.view_employee(res)
# res.menu.show_menu()

# # Create a customer and interact
# c1 = Customer("Rakib", "rakib@email.com", 123456, "Mirpur")
# c1.view_menu(res)


# item_name= input("enter item name: ")
# item_quantity=int(input("enter item quantity: "))

# c1.add_to_cart(res, item_name, item_quantity)
# c1.view_cart()
