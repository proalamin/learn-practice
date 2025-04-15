class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):  # Method overriding
        print("Dog barks")

d = Dog()
d.speak()  # Output: Dog barks
