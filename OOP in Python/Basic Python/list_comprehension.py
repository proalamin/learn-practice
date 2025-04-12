numbers = [34, 45, 33, 23, 23, 23, 12, 11, 45, 56, 67, 78, 89, 90]

ods=[]

for num in numbers:
    if num % 2 == 1:
        ods.append(num)
print(ods) # [45, 23, 23, 11, 67, 89]

ods_numbers = [num for num in numbers if num % 2 == 1]
print(ods_numbers) # [45, 23, 23, 11, 67, 89]
# The above two snippets are equivalent

