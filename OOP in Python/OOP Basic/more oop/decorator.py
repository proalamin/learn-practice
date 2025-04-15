# A decorator is a function that takes another function, adds extra behavior, and returns a new function.


def timer(func):
    def inner():
        print('time started...')
        func()
        print('time end...')
    return inner

# timer()()

@timer
def get_factorial():
    print('factorial starting')

get_factorial()