def call():
    print("Calling...")
    return 'call done'

class Phone:
    price = 12000
    color = "black"
    brand = "Samsung"
    features = ["4G", "5G", "WiFi", "Bluetooth"]

    def call(self):  # in python when in class add a function/method need to add a extra parameter 'self;
        print('calling someone')

    def send_msg(self, phoneNumber, sms):
        text = f'sending SMS to : {phoneNumber} and message:{sms}'
        return text

my_phone = Phone()
print(my_phone.features)
my_phone.call()
output = my_phone.send_msg(234325235, "Dear Mr/Mrs, \nWe are happy to inform you, you are selected :)")
print(output)