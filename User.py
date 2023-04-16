
print("*" * 30 + "User Details" + "*" * 30 + "\n")

from datetime import datetime
import sys
import random
import json
import time

print("Date:", datetime.now())
print("@Author : Balreddy")


class User:
    def __init__(self):
        # print("+="*70)
        self.register = {}
        self.id = "1"

    def registration(self):
        name = input("Enter Your Name :")
        mobile = int(input("Enter Your Mobile No :"))
        address = input("Enter Your Address :")
        email = input("Enter Your Mail ID :")
        password = (input("Enter Your Password :"))
        details = {"Name": name, "Mobile": mobile, "Address": address, "Email ID": email, "Password": password}
        self.register[self.id] = details
        with open("Register.json", "w") as f:
            json.dump(self.register, f, indent=4)
            print("Registered Successfully...!")
            time.sleep(5)
            print()
            print(self.register)
            print("Your Email ID and Password is Your Login ID and Password")
            return "Now Login"

    def login(self, email, password):
        with open("Register.json", "r") as f:
            self.item = json.load(f)
        if email == self.item[self.id]["Email ID"]:
            if password == self.item[self.id]["Password"]:
                return "Login Successfully...!"
            else:
                return "Invalid Password Login Again ❌"
        else:
            print("Your Customer is not Exiting.\n")
            time.sleep(2)
            print("You have to Registered First")
            return ""

    def update_profile(self):
        print(" - "*100)
        print("------->>>Press 1 for Update Name")
        print("------->>>Press 2 for Update Mobile Number")
        print("------->>>Press 3 for Update Address")
        print("------->>>Press 4 for Update Email ")
        print("------->>>Press 5 for Update Password")
        print("------->>>>Press 0 for exit")
        print(" - "*100)
        press = input("Please Enter a Button :")

        if press == "1":
            name = input("Enter Your Update Name: ")
            self.item[self.id]['Name'] = name
            with open("Register.json", "w") as f:
                json.dump(self.item, f, indent=4)
            print("Your Updated Profile is", self.item[self.id])

        if press == "2":
            mobile = input("Enter Your Update Mobile :")
            self.item[self.id]['Mobile'] = mobile
            with open("Register.json", "w") as f:
                json.dump(self.item, f, indent=4)
            print("Your Updated Profile is", self.item[self.id])

        if press == "3":
            address = input("Enter Your Update Address :")
            self.item[self.id]['Address'] = address
            with open("Register.json", "w") as f:
                json.dump(self.item, f, indent=4)
            print("Your Updated Profile is", self.item[self.id])

        if press == "4":
            email = input("Enter Your Update Email Id :")
            self.item[self.id]['Email'] = email
            with open("Register.json", "w") as f:
                json.dump(self.item, f, indent=4)
            print("Your Updated Profile is", self.item[self.id])

        if press == "5":
            password = input("Enter Your Update Password :")
            self.item[self.id]['Password'] = password
            with open("Register.json", "w") as f:
                json.dump(self.item, f, indent=4)
            print("Your Updated Profile is", self.item[self.id])

        if press == "0":
            time.sleep(5)
            print("Your Profile is Updated ")
            sys.exit()

x = User()
x.registration()
x.login("balu123@gmail.com", "balu123")
x.update_profile()