from food_item import FoodItem
from menu import Menu
from users import Customer, Admin, Employee
from restaurant import Restaurant
from orders import Order

mamar_res = Restaurant("Mamar Restaurant")

def cusmtomer_menu():
    name = input("enter your name: ")
    email= input("enter your email: ")
    phone = input("enter your phone: ")
    address = input("enter your address: ")

    customer = Customer(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"Welcome {customer.name}!!")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. PayBill")
        print("5. Exit")

        choice = int(input("enter your choice: "))
        if choice == 1:
            customer.view_menu(mamar_res)
        elif choice == 2:
            item_name= input("enter item name: ")
            item_quantity=int(input("enter item quantity: "))
            customer.add_to_cart(mamar_res, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            print("log out...")
            break
        else:
            print("invalid input")

def admin_menu():
    name = input("enter your name: ")
    email= input("enter your email: ")
    phone = input("enter your phone: ")
    address = input("enter your address: ")

    admin = Admin(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"Welcome {admin.name}!!")
        print("1. Add new item")
        print("2. Add new employee")
        print("3. View employee")
        print("4. View Items")
        print("5. Delete Items")
        print("6. Exit")

        choice = int(input("enter your choice: "))
        if choice == 1:
            item_name = input("enter item name: ")
            item_price = int(input("enter item price: "))
            item_quantity = int(input("enter item quantity: "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(mamar_res, item)

        elif choice == 2:
            name = input("enter employee name: ")
            phone = input("enter employee phone: ")
            email = input("enter employee email: ")
            designation = input("enter employee designation: ")
            age = input("enter employee age: ")
            salary = input("enter employee salary: ")
            address = input("enter employee address: ")
            admin.add_employee(name, email, phone, address, age, designation, salary)

        elif choice == 3:
            admin.view_employee(mamar_res)

        elif choice == 4:
            admin.view_menu(mamar_res)

        elif choice == 5:
            item_name= input('"enter item name: ')
            admin.del_item(mamar_res, item_name)
        elif choice == 6:
            print("log out...")
            break
        else:
            print("invalid input")