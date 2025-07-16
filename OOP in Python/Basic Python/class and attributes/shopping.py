class Shopping:
    def __init__(self, buyer_name):
        self.buyer_name = buyer_name
        self.cart =[]

    def add_to_cart(self, item, price, quantity):
        product ={'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def checkout(self, ammount):
        total =0
        for item in self.cart:
            # print(item)
            total += item['price'] * item['quantity']
        print('total price', total)
        if ammount < total:
            print(f'please provide more {total - ammount}')
        else:
            extra = ammount - total
            print(f'extra amount is {extra}')


swapan = Shopping('alan swapan')
swapan.add_to_cart('alu', 25, 2)
swapan.add_to_cart('dim', 15, 10)
swapan.add_to_cart('morich', 0.5, 50)


print(swapan.cart)
swapan.checkout(600)