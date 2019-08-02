from crazyshit import db
from datetime import datetime

#users = {"user_one": [1234, 2000], "user_two": [2222, 1277], "user_three": [3333, 66]}
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    pin = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Integer)
    #created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #account = db.relationship('Account', backref='owner',lazy=True)

    def __repr__(self):
        return f"User(name='{self.name}', pin='{self.pin}', balance='{self.balance}')"
    #def __repr__(self):
    #    return f"User(name='{self.name}', pin='{self.name}', created_at='{self.created_at}')"

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    owner_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Account(balance='{self.balance}', owner='{self.owner_id}', created_at='{self.created_at}')"


'''
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
'''
