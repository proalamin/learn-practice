class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 500
        self.max_withdraw = 200000
    
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'after deposit balance is {self.get_balance()}')
    
    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f'minimum withdraw balance {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f'maximum withdraw balance {self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'after withdraw available account balance {self.get_balance()}')


tor_bank = Bank(32000)
tor_bank.withdraw(4000)

avai_balance=tor_bank.get_balance()
print(f'check: available balance is now {avai_balance}')
tor_bank.deposit(400)

avai_balance=tor_bank.get_balance()
print(f'check: available balance is now {avai_balance}')


