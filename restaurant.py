"""Describes a restaurant and its cuisine."""

class Restaurant:
    """Models a restaurant. 
    Has methods that state the name, cuisine type, and a message saying it's open."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is named {self.restaurant_name} and it serves {self.cuisine_type} food. ")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open! ")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name, cuisine_type,flavors):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = flavors

    def display_flavors(self):
        print(f"{self.restaurant_name} serves ice cream. The following ice cream flavors are available: {self.flavors}")

