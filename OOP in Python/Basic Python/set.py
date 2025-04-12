# list --> []
# tuple --> ()
# set --> {}    # set unique items from a list. No duplicates

numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)
# Output: {1, 2, 3, 4, 5}

unique_numbers.add(6)
print(unique_numbers)
# Output: {1, 2, 3, 4, 5, 6}  

unique_numbers.remove(1)
print(unique_numbers)
# Output: {2, 3, 4, 5, 6}
unique_numbers.discard(2)
print(unique_numbers)
# Output: {3, 4, 5, 6} 


A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)  # Union #output: {1, 2, 3, 4, 5}
print(A & B)  # Intersection #output: {3}
print(A - B)  # Difference #output: {1, 2}
print(A ^ B)  # Symmetric Difference #output: {1, 2, 4, 5}

print(A.issubset(B))  # Subset #output: False
print(A.issuperset(B))  # Superset #output: False
print(A.isdisjoint(B))  # Disjoint #output: False
print(A.pop())  # Remove and return an arbitrary element #output: 1
print(A.clear())  # Clear the set #output: None