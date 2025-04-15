"""
Getter -> A method that returns the value of a private attribute using @property.

Setter -> A method that sets or updates a private attribute using @attribute.setter.

read only -> A property that only has a getter and no setter, so its value can be read but not modified.

"""

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):  # Getter 
        return self._name

    @name.setter
    def name(self, value):  # Setter
        if len(value) >= 2:
            self._name = value
        else:
            print("Name too short!")

p = Person("Alice")
print(p.name)       # Getter is called

p.name = "Bo"       # Setter is called
print(p.name)
p.name = "A"        # Invalid


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):  # Getter only
        return self._name

# No setter defined — so it's read-only!

p = Person("Alice")
print(p.name)     # ✅ OK
p.name = "Amin"   # ❌ Error: can't set attribute
