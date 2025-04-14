class Shop:
    # products = [] # Class attribute -> Shared by all instances of the class.

    def __init__(self, name):
        self.name = name
        self.products =[] # Instance attribute -> Belongs to the individual object, each object can have different values.

    def __repr__(self): # dander methods
        return f'shope name: {self.name}'

    def addProduct(self, name, price):
        product = Product(name, price)
        self.products.append(product)

    # def __str__(self): # # dander methods str output first
    #     return f'welcome to {self.name}'

class Product:
    def __init__(self, name, price):
        self.name=name
        self.price = price

    def __repr__(self):
        return f"product name: {self.name}, price: {self.price}"
    

shop1 = Shop('shop_1') # object
shop1.addProduct('tui phone', 123131)
shop1.addProduct('tui laptop', 342342)

shop2 = Shop('shop_2')
shop2.addProduct('mouse', 1200)

print(shop1)
print(shop1.products)

print(shop2)
print(shop2.products)
