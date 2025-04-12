firstNumber =int(input())
secondNumber =int(input())
thirdNumber =int(input())

if firstNumber > secondNumber and firstNumber > thirdNumber:
    print(f"first number is big {firstNumber}")
elif secondNumber > firstNumber and secondNumber > thirdNumber:
    print(f"second number is big {secondNumber}")
else:
    print(f"third number is big {thirdNumber}")

sum = firstNumber + secondNumber + thirdNumber
print("sum of input number", sum)


# run a loop and print odd number 39 to 68
start =39
while start <= 68:
    start +=1
    if start % 2 !=1:
      continue 
    print(start)