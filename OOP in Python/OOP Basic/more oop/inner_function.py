def outer():
    print("I'm the outer function")
    
    def inner():
        print("I'm the inner function")
    inner()  # Call inner inside outer

outer()


def something(work):
    print('something....')
    work()  # Calling the function passed

def work():
    print('working..')

something(work)  # Passing function, not calling it


