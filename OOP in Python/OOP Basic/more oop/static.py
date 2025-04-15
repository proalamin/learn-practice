class Student:
    school_name = "ABC School"  # Static/Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute


s1 = Student("Alice")
s2 = Student("Bob")

# print(s1.school_name)  # ABC School
# print(s2.school_name)  # ABC School

Student.school_name = "XYZ School" ## Changing static/class attribute

# print(s1.school_name)  # XYZ School (changed for all)


"""
------>Static Method<-------
Does not take self or cls.
Acts like a normal function but is grouped inside the class for organization.
Cannot access instance or class attributes directly.

You can call it directly using ClassName.method() or object.method()
No need to create an object if only static methods are used.
"""

class Math:

    @staticmethod
    def add(a, b):  # No self or cls
        return a + b

print(Math.add(3, 4))  # Output: 7


"""
-------> Class Method <-------
Uses cls as the first parameter.
Can access class-level data (like static/class attributes).
Can modify class variables.
Often used to create alternative constructors.

Used when you need to work with or change class data.
You pass the class itself (cls) instead of the object.
"""

class Student:
    total_students = 0  # Class Attribute (shared)

    def __init__(self, name):
        self.name = name  # Instance attribute
        Student.total_students += 1  # Increase total for every new student

    @classmethod
    def getTotalStudents(cls):
        return cls.total_students  # Access class attribute using cls

s1 = Student("Alice")
s2 = Student("Bob")

print(Student.getTotalStudents())  # Output: 2
