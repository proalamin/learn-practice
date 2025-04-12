# built in modules  
# import os
# import sys

# import math
from math import *
result =ceil(2.3)
print(result) #output: 3 

result = floor(2.3)
print(result) #output: 2

# import random
from random import *
result = random()
print(result) #output: give a random number

result = randint(1001, 1913)
print(result) #output: random number between 1001 and 1913

#there is no possible a number more then once time
from random import sample
winners = sample(range(1, 6), 5)  # 1914 because end is exclusive
for i, num in enumerate(winners, 1):
    print(f"{i} winner:", num) 

print()
# there is possible a number more then once time
num = 1
while num <= 5:
    result = randint(1, 5)
    print(f"{num} winner:", result) 
    num += 1


# import datetime
# import time
# import re
# import json
# import urllib
# import requests   