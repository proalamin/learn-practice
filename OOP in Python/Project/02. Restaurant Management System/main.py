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
            break
        else:
            print("log out...")