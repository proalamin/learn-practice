def full_name(first, second, **last):
    name = f'{first} {second} {last.get("last", "")}'
    print(last)  # {'last': 'kumra'}
    return name

name = full_name(first='alu', second='kodu', last='kumra')
print(name) # alu kodu kumra

def a_lot(num1, num2):
    sum = num1 + num2
    multi = num1 * num2
    remain = num1 - num2
    return [sum, multi, remain] #list
    return sum, multi, remain # tuples

everything = a_lot(55, 21)
print(everything) #[76, 1155, 34]