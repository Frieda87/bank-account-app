'''from flask import Flask

app = Flask(__name__)

list_pins = {"user_one": 1234, "user_two": 2222, "user_three": 3333}
list_with_pins = {("user_one", 1234): 2000, ("user_two", 2222): 1277, ("user_three", 3333): 66}

@app.route('/balance')
def display_balance(pin_number, user_name):
    balance = 200
    if pin_number == list_pins[user_name]:
        return "Your balance is {} Euro.".format(balance)
    else:
        return pin_error

@app.route('/withdrawn')
def withdraw_money(pin_number, user_name, amount):
    for x, y in list_with_pins.items():
        if x[0] == user_name and x[1] == pin_number:
            if amount <= y:
                y -= amount
                return "Withdrew {} EUR. New balance is: {} EUR.".format(amount, y)
        else:
            return "You are not allowed to withdraw more money than you have on your account!"
    else:
        return pin_error

from flask import Flask, request

app = Flask(__name__)

user_data = {'user1': ['1234', 2000], 'user2': ['5576', 3000], 'user3': ['2293', 200]}

# http://127.0.0.1:5000/balance?pin=1234&user=user2
# try to play with the above mentioned url :)
@app.route('/balance')
def display_balance():
    pin_number = request.args.get('pin') # instead of writing a pin as argument, we use this line of code. why?
    user = request.args.get('user') # instead of writing a pin as argument, we use this line of code. why?
    if pin_number == user_data[user][0]:
        return 'This is your current balance: {} EUR'.format(user_data[user][1])
    else:
        return pin_error()

def pin_error():
    return 'Access denied: incorrect PIN.'

# http://127.0.0.1:5000/withdraw?pin=1234&user=user1&amount=50
# try to play with the above mentioned url :)
@app.route('/withdraw')
def withdraw_money():
    pin_number = request.args.get('pin') # instead of writing a pin as argument, we use this line of code. why?
    user_name = request.args.get('user') # instead of writing a pin as argument, we use this line of code. why?
    amount = request.args.get('amount') # instead of writing a pin as argument, we use this line of code. why?
    amount = int(amount) # why does this have to be transformed into integer?

    balance = user_data[user_name][1]
    if pin_number == user_data[user_name][0]:
        if amount <= balance:
            balance = balance - amount
            return 'Withdrew {} EUR. New balance is: {} EUR.'.format(amount, balance)
        else:
            return 'You are not allowed to withdraw more money than you have on your account!'
    else:
        return pin_error()'''

from crazyshit import app, Blueprint
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL= '/swagger'
API_DOC_URL='/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_DOC_URL,
    config={
        'app_name':'Banking App'
    }
)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)


if __name__ == '__main__':
    app.run(debug = True)