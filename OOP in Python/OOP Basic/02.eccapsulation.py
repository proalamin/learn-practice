class Shop:

    def __init__(self, name):
        self.name = name
        self.products =[]
        self.__balance = 2300 # private attribute
        self._owner = 'Mr. X' # protected attribute

    def get_balance(self):  # get output private attribute
        return f'balance: {self.__balance}'

    def __repr__(self):
        return f'shope name: {self.name}'

    def addProduct(self, name, price):
        product = Product(name, price)
        self.products.append(product)


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
print(shop1.get_balance())


print(shop2)
print(shop2.products)

"""
Access modifier
1.public
2.private
3.protected

"""