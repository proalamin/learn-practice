# singleton --> one single instance
# if you want a new instance, you will get the the ole one (already created) instance

class Singleton:
    _instance = None
    def __init__(self):
        if Singleton._instance is None:
            Singleton._instance = self
        else:
            raise Exception('this is Singleton.')
        

    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            Singleton()
        return Singleton._instance
    
first = Singleton.get_instance()
second = Singleton.get_instance()
third = Singleton.get_instance()

print(first)
print(second)
print(third)
