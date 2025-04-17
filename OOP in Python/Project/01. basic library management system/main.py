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

    def __init__(self, name):
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


