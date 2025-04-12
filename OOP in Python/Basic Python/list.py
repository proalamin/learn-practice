# list --> []
# tuple --> ()
# set --> {}    # set unique items from a list. No duplicates
numbers =[34,45,33,23,23,23,12,11,45,56,67,78,89,90]

print(numbers[1], numbers[-1])


# lst ( start : end) start from the start index and stops before the end index
print(numbers[1:5]) # [45, 33, 23, 23]


print(numbers[:5]) # [34, 45, 33, 23, 23]
print(numbers[5:]) # [23, 12, 11, 45, 56, 67, 78, 89, 90]
print(numbers[::2]) # [34, 33, 23, 12, 45, 67, 89]  



# list[start:end:step] start from the start index and stops before the end index and takes every step index
print(numbers[1:5:2]) # [45, 23]
print(numbers[1::3]) # [45, 23, 45, 89]
print(numbers[::-2]) # [90, 78, 56, 23, 11, 34]       

# lst[:] gives a shallow copy of the list
print(numbers[:]) # [34, 45, 33, 23, 23, 23, 12, 11, 45, 56, 67, 78, 89, 90]

#short cut reverse the list
print(numbers[::-1]) # [90, 89, 78, 67, 56, 45, 11, 12, 23, 23, 23, 33, 45, 34] 

