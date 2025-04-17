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

    def addBooks(self, id, name, quan):
        
        for book in self.books:
            if book.id == id:
                print('this book already exists')
                return

        books = Book(id, name, quan)
        self.books.append(books)

        print(f'{book.name} is successfully added')


    def add_user(self, id, name, pas):

        for user in self.users:
            if user.id == id:
                print('already you are a user')
                return

        user = User(id, name, pas)
        self.users.append(user)

        print('f{user.name} new user added')
    