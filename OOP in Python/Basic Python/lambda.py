
def sum(x, y):
    return x + y
ans = sum(1, 2)
print(ans) #output: 3

# lambda function
sum = lambda x, y: x + y
ans = sum(1, 2)
print(ans) #output: 3

# lambda function with multiple arguments
sum = lambda x, y, z: x + y + z
ans = sum(1, 2, 3)
print(ans) #output: 6

# lambda function with default arguments
sum = lambda x, y=2: x + y
ans = sum(1)
print(ans) #output: 3



numbers = [1, 2, 3, 4, 5]
double_num = map(lambda x: x * 2, numbers)
print(list(double_num)) #output: [2, 4, 6, 8, 10]

# lambda function with filter
numbers = [1, 2, 3, 4, 5]
even_num = filter(lambda x: x % 2 == 0, numbers)
print(list(even_num)) #output: [2, 4]           