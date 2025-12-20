"""
foodItem (name, price)
burger (foodItem)
pizza (foodItem)
drink (foodItem)
"""

from abc import ABC, abstractmethod


class FoodItem(ABC):
    def __init__(self, name, price):
        self.__name=name
        self.__price=price
        
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    @abstractmethod
    def prepare(self):
        pass
        
class Burger(FoodItem):
    def __init__(self):
        super().__init__("Large Burger", 600)
        
    def prepare(self):
        print("preparing burger....")

class Pizza(FoodItem):
    def __init__(self):
        super().__init__("12inch Pizza", 900)
        
    def prepare(self):
        print("preparing pizza....")
        
class Drink(FoodItem):
    def __init__(self):
        super().__init__("1L Drink", 130)
    
    def prepare(self):
        print("preparing drink....")
        
        

burger= Burger()
print(burger.get_name(), burger.get_price(),burger.prepare(), "\n")

pizza= Pizza()
print(pizza.get_name(), pizza.get_price(), pizza.prepare(),"\n")
