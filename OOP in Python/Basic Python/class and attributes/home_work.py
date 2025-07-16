class Calculator:
    brand = 'Casio MS990'

    def add(self, num1, num2):
        ans= num1+num2
        return ans
    
    def deduct(self, num1, num2):
        ans= num1-num2
        return ans
    
    def multi(self, num1, num2):
        ans= num1*num2
        return ans
    
    def devide(self, num1, num2):
        ans= num1/num2
        return ans
    
my_cal = Calculator()
sum = my_cal.add(2,4)
deduct = my_cal.deduct(2,4)
multi = my_cal.multi(2,4)
divide = my_cal.devide(2,4)

print(sum)
print(deduct)
print(multi)
print(divide)