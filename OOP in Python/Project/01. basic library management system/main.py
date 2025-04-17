class Book:

    def __init__(self, id, name, quantity):
        self.id = id
        self.name= name
        self.quantity = quantity


class User:

    def __init__(self, id, name, password):
        self.id = id
        self.name= name
        self.password = password
        self.borrowedBooks=[]
        self.returnedBooks=[]

class Library:

    def __init__(self, name):
        self.name= name
        self.users=[]
        self.books=[]

    def addBooks(self, id, name, quan):
        
        for book in self.books:
            if book.id == id:
                print('this book already exists')
                return

        book = Book(id, name, quan)
        self.books.append(book)

        print(f"new book added : {book.name} ")

        return book


    def add_user(self, id, name, pas):

        for user in self.users:
            if user.id == id:
                print('already you are a user')
                return

        user = User(id, name, pas)
        self.users.append(user)

        print(f"new user added : {user.name} ")

        return user

    def borrowBook(self, user, bookId, date):

        for book in self.books:
            if book.id == bookId:
                if book in user.borrowedBooks:
                    print('already this book borrowed')
                    return
                elif book.quantity < 1:
                    print('now available copies')
                    return
                else:
                    user.borrowedBooks.append(book)
                    book.quantity -=1
                    print('borrowed successfully')
                    return
        print(f'not sound this book id {bookId}')
    

    def returnBook(self, user, bookId, date):

        for book in self.books:
            if book.id == bookId:
                if book in user.borrowedBooks:
                    book.quantity +=1
                    user.borrowedBooks.remove(book)
                    user.returnedBooks.append(book)
                    return
                else:
                    print('you did now borrow this book')
                    return
        print(f'not sound this book id {bookId}')


myLibrary = Library('my library')
admin = myLibrary.add_user(1,'admin', "pass")
user2 = myLibrary.add_user(2, 'user 2', '22222')

dsa = myLibrary.addBooks(1, 'data structure and algorithm', 700)
