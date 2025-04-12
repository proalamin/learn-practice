class Phone:
    manufactured = "China"

    def __init__(self, owner, brand, price,):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self, phoneNumber, sms):
        text = f'sending to: {phoneNumber}, {sms}'
        print(text)

myPhone = Phone('Chad Babu', 'Tui Phone', 121131)
print(myPhone.owner, myPhone.brand, myPhone.price)


info= myPhone.send_sms(2312312, 'your phone ready to collect..')