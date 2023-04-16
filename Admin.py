from datetime import datetime
import random
import time
import json
import sys

class Admin:
    def __init__(self):
        self.food_item = {}
        self.food_id = len(self.food_item) + 1
        self.food_item = {}


    def new_food_item(self):
        self.name = input("Enter Food Item Name: ")
        self.quantity = int(input("Enter Food Quantity is: "))
        self.price = int(input("Enter Food Price is: "))
        self.stock = int(input("Enter Food Stock is: "))
        self.discount = int(input("Enter Food Discount is: "))
        self.item = {"Food Name": self.name, "Quantity": self.quantity, "Price": self.price, "Stock": self.stock, "Discount": self.discount}
        self.food_id = len(self.food_item) + 1
        self.food_item[self.food_id] = self.item
        with open("Food Item.json", "w") as f:
            json.dump(self.food_item, f, indent=5)
        return self.food_item

    def edit_food_item(self):
        self.food_item[3]["Food Name"] = "Chi. Biryani"
        self.food_item[3]["Quantity"] = 1
        self.food_item[3]["Price"] = 250
        self.food_item[3]["Stock"] = 100
        self.food_item[3]["Discount"] = 5
        return self.food_item[3]

    def view_food_item(self):
        return list(self.food_item.items())

    def remove_food_item(self):
        food_item = int(input("I want remove Food ID: "))
        del self.food_item[food_item]
        self.food_id = len(self.food_item) + 1
        print("Updated Food Item is: ", self.food_item)
        with open("Food Item.json", "w") as f:
            json.dump(self.food_item, f, indent=5)
        return ""


c = Admin()
print(c.new_food_item())
print(c.new_food_item())
print(c.new_food_item())
print(c.new_food_item())
print("*"*25)
print(c.edit_food_item())
print("*"*25)
print("List of Food Items:", c.view_food_item())
print("*"*25)
print(c.remove_food_item())
print("*"*25)
print("Updated List of Food Items:", c.view_food_item())

print("\t\t\t  ******Thank You Visit...!  \t\t\t")