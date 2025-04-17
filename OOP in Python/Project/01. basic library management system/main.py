class Book:

    def __init__(self, name, id, quantity):
        self.name= name
        self.id = id
        self.quantity = quantity


class User:

    def __init__(self, id, name, password):
        self.id = id
        self.name= name
        self.password = password
        self.borrowedBooks=[]
        self.returnedBooks=[]

class Library:

    def __init__(self, name, password):
        self.name= name
        self.users=[]
        self.books=[]

    