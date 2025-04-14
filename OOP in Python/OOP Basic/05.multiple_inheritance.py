class Watch:  #parent /supporior
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print('watch')

    def display_time(self):
        print('time now..')

class FitnessTracker:
    def __init__(self, price):
        self.price = price
        print('fitness tracker')

    def track_step(self):
        print("tracking....")
    
    def track_calories(self):
        print("tracking calories")


class SmartWatch(Watch, FitnessTracker):
    def __init__(self, brand, model, price):
        Watch.__init__(self,brand, model)
        FitnessTracker.__init__(self, price)


apple_watch =SmartWatch('apple', 'watch 4', 24333)
print(apple_watch.brand, apple_watch.model, apple_watch.price)


# MRO - method rajulation order