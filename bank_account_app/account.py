'''list_with_pins = {"user_one": 1234, "user_two": 2222, "user_three": 3333}

balance = 100
pin_error = "Your pin is incorrect."

def display_balance(pin_number, user_name):
        if pin_number == list_with_pins[user_name]:
            return "Your balance is {} Euro.".format(balance)
        else:
            return pin_error

print(display_balance(1234, "user_one"))
print(display_balance(1728, "user_one"))

## Write a similar function called 'withdraw_money'
## withdraw_money should have 2 args 'pin_number' and 'amount'
## 1. check if pin is correct, if not return the error
## 2. check if amount is smaller or equal to balance, if so: substract the amount and return e.g. 'Withdrew 30 EUR. New balance is: 2000 EUR.
## otherwise return 'You are not allowed to withdraw more money than you have on your account!'

def withdraw_money(pin_number, user_name, amount):
    balance = 100
    if pin_number == list_with_pins[user_name]:
        if amount <= balance:
            balance -= amount
            return "Withdrew {} EUR. New balance is: {} EUR.".format(amount, balance)
        else:
            return "You are not allowed to withdraw more money than you have on your account!"
    else:
        return pin_error

print(withdraw_money(1234, "user_one", 140))

list_pins = {"user_one": 1234, "user_two": 2222, "user_three": 3333}
list_with_pins = {"user_one": [1234, 2000], "user_two": [2222, 1277], "user_three": [3333, 66]}


def display_balance(pin_number, user_name):
    balance = list_with_pins[user_name][1]
    if pin_number == list_with_pins[user_name][0]:
        return "Your balance is {} Euro.".format(balance)
    else:
        return "Your pin is incorrect."


def withdraw_money(pin_number, user_name, amount):
    balance = list_with_pins[user_name][1]
    if pin_number == list_with_pins[user_name][0]:
        if amount <= balance:
            balance -= amount
            return "Withdrew {} EUR. New balance is: {} EUR.".format(amount, balance)
        else:
            return "You are not allowed to withdraw more money than you have on your account!"
    else:
        return "Your pin is incorrect."'''

class Account:
    user_data = {"user_one": [1234, 2000], "user_two": [2222, 1277], "user_three": [3333, 66]}
    def __init__(self, user_name, pin_number):
        self.user_name = user_name
        self.pin_number = pin_number
        
    def display_balance(self):
        balance = self.user_data[self.user_name][1]
        if self.pin_number == self.user_data[self.user_name][0]:
            return "Your balance is {} Euro.".format(balance)
        else:
            return "Your pin is incorrect."

    def withdraw_money(self, amount):
        balance = self.user_data[self.user_name][1]
        if self.pin_number == self.user_data[self.user_name][0]:
            if amount <= balance:
                balance -= amount
                return "Withdrew {} EUR. New balance is: {} EUR.".format(amount, balance)
            else:
                return "You are not allowed to withdraw more money than you have on your account!"
        else:
            return "Your pin is incorrect."

'''import Flask from flask
import account from models


app = Flask(__name__)

'''

account1 = Account("user_one", 1234)

print(account1.display_balance())
print(account1.withdraw_money(50))'''
