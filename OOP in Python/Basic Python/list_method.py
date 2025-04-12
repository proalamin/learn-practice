# Python List Methods - Examples and Usage

# 1. append() - Adds an element at the end of the list
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(f"After append: {fruits}") # Output: ['apple', 'banana', 'cherry', 'orange']

# 2. extend() - Adds all elements of a list (or any iterable) to the end of the current list
vegetables = ['carrot', 'potato']
fruits.extend(vegetables)
print(f"After extend: {fruits}") # Output: ['apple', 'banana', 'cherry', 'orange', 'carrot', 'potato']

# 3. insert(position, value) - Inserts an element at a specified position
fruits.insert(1, 'grape')
print(f"After insert: {fruits}") # Output: ['apple', 'grape', 'banana', 'cherry', 'orange', 'carrot', 'potato']

# 4. remove() - Removes the first occurrence of the specified element
fruits.remove('banana')
print(f"After remove: {fruits}") # Output: ['apple', 'grape', 'cherry', 'orange', 'carrot', 'potato']
if 'banana' not in fruits:
    print("Banana has been removed from the list.") # Output: Banana has been removed from the list.
# Note: If the element is not found, it raises a ValueError

# 5. pop() - Removes the element at the specified position (or the last item if no index is specified)
popped_item = fruits.pop()
print(f"After pop: {fruits}, Popped item: {popped_item}")

# 6. clear() - Removes all elements from the list
fruits.clear()
print(f"After clear: {fruits}")

# 7. index() - Returns the index of the first occurrence of the specified element
numbers = [10, 20, 30, 40, 50]
index_of_30 = numbers.index(30)
print(f"Index of 30: {index_of_30}")

# 8. count() - Returns the number of elements with the specified value
count_of_20 = numbers.count(20)
print(f"Count of 20: {count_of_20}") # Output: 1

# 9. sort() - Sorts the list in ascending order (or descending if reverse=True is specified)
numbers.sort()
print(f"Sorted list: {numbers}") # Output: [10, 20, 30, 40, 50]
numbers.sort(reverse=True)
print(f"Reverse sorted list: {numbers}") # Output: [50, 40, 30, 20, 10]

# 10. reverse() - Reverses the order of the list
numbers.reverse()
print(f"Reversed list: {numbers}") # Output: [10, 20, 30, 40, 50]

# 11. copy() - Returns a shallow copy of the list
numbers_copy = numbers.copy()
print(f"Copied list: {numbers_copy}") # Output: [10, 20, 30, 40, 50]