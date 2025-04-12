class Shop:
    shopping_mall = 'Jamuna'
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []  #cart is an instance attribute

    
    def add_to_cart(self, item):
            self.cart.append(item)

mehjabenn = Shop('mehjabenn eid shopping')
mehjabenn.add_to_cart('t-pis')
mehjabenn.add_to_cart('aro onak kichu kincha jani na')
print(mehjabenn.cart)

niso = Shop('niso shopping kortacha')
niso.add_to_cart('watch')
niso.add_to_cart('shirt')
print(niso.cart)

apurbo = Shop('apurbo shopping')
apurbo.add_to_cart('shoes')
print(apurbo.cart)