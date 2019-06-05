#from crazyshit import user_data
#user_data = {"user_one": [1234, 2000], "user_two": [2222, 1277], "user_three": [3333, 66]}
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
