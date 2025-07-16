class Shop:
    cart = []
    def __init__(self, buyer):
        self.buyer = buyer


    def add_to_cart(self, item):
        self.cart.append(item)


mehzabin = Shop('meh')
mehzabin.add_to_cart('shoes')
print(mehzabin.cart)
