numbers = [34, 45, 33, 23, 23, 23, 12, 11, 45, 56, 67, 78, 89, 90]

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# Accessing values
print(person.keys())  # Output: dict_keys(['name', 'age', 'city'])
print(person["name"])  # Output: John
print(person["name"], person["age"])  # Output: John 30

print(person.values())  # Output: dict_values(['John', 30, 'New York'])

person['language'] = 'English'  # Add a new key-value pair 
print(person)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'language': 'English'}

del person['age']  # Delete a key-value pair
print(person)  # Output: {'name': 'John', 'city': 'New York', 'language': 'English'}

# special dectionary looping
for key, value in person.items():
    print(f"{key}: {value}")
# Output:
# name: John
# age: 30 
# city: New York
#language: English