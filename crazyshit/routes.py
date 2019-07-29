from flask import request, jsonify, abort, request
from crazyshit.models import User
from crazyshit import app, db
from crazyshit.schemas import UserSchema

#user_data = {'user1': ['1234', 2000], 'user2': ['5576', 3000], 'user3': ['2293', 200]}

@app.route('/')
def home_page():
    return 'This is a bank account app!!!'

# http://127.0.0.1:5000/balance?pin=1234&user=user2
# try to play with the above mentioned url :)
@app.route('/users/<int:user_id>/balance', methods=['GET'])
def display_balance(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        user_schema = UserSchema()
        response = user_schema.dump(user.balance).data
        return jsonify(response)
    else:
        abort(404, description="User does not have an account yet")


# http://127.0.0.1:5000/users/:user_id/withdraw

# PATCH : http://127.0.0.1:5000/users/:user_id/withdraw



@app.route("/users/<int:user_id>/accounts", methods=["POST"])
def create_account(user_id):
    data = request.get_json(force=True)  # force=True will make sure this works even if a client does not specify application/json
    validate(instance=data, schema=account_request_schema)
    balance = data["balance"]
    user = User.query.get_or_404(user_id, "User does not exist")
    account = Account(balance=balance, owner_id=user_id)
    db.session.add(account)
    db.session.commit()
    account_schema = AccountSchema()
    response = account_schema.dump(account).data
    return jsonify(response)

#1
@app.route('/users/<int:user_id>/deposit', methods=["PATCH"])
def deposit_money(user_id):
    data = request.get_json(force=True)
    amount = data['amount']
    pin = data['pin']
    if amount > 3000:
        abort(400, description="You cannot deposit more than the 3000 Euro a day.")
    else:
        user = User.query.get_or_404(user_id, "User does not exist.")
        if pin == int(user.pin):
            user.balance += amount
            db.session.commit()
            user_schema = UserSchema()
            response = user_schema.dump(user).data
            return jsonify(response)
        else:
            abort(400, description="The pin was incorrect.")
            
#2
@app.route('/users/<int:user_id>/withdraw', methods=['PATCH'])
def withdraw(user_id):
    data = request.get_json(force=True)
    amount = data["amount"]
    pin = data["pin"]
    if amount > 2000:
        abort(400, description='You are not allowed to go over 2000 euro daily limit') 
    else:
        user = User.query.get_or_404(user_id, "User does not exist")
        if pin == int(user.pin): 
            if amount <= user.balance:
                user.balance -= amount
                db.session.commit()
                user_schema = UserSchema()
                response = user_schema.dump(user).data
                return jsonify(response)       
            else:
                abort(400, description="You are not allowed to withdraw more money than you have on your account!")
        else:
            abort(400, description="Pin is not correct")
#3
@app.route('/users/<int:user_id>/transfer', methods=['PATCH'])
def transfer_money(user_id):
    data = request.get_json(force=True)
    pin = data['pin']
    amount = data['amount']
    receiver_id = data['receiver_id']
    sender = User.query.get_or_404(user_id, description="Account holder does not exist.")
    if pin == int(sender.pin):
        if amount <= sender.balance:
            receiver = User.query.get_or_404(receiver_id, "Receiver does not exist.")
            sender.balance -= amount
            receiver.balance += amount
            db.session.commit()
            user_schema = UserSchema()
            response_sender = user_schema.dump(sender).data
            response_receiver = user_schema.dump(receiver).data
            return jsonify(response_sender, response_receiver)
        else:
            abort(400, description="You are not allowed to withdraw more money than you have in your bank account.")
    else:
        abort(400, description="The pin was incorrect.")


'''@app.route('/users/<int:user_id>/transfer', methods=['PATCH'])
def transfer(user_id):
    data = request.get_json(force=True)
    amount = data["amount"]
    pin_number = data["pin"]
    receiver_id = data["receiverId"]
    if amount >= 3000:
        abort(400, description='You are not allowed to go over 3000 euro daily limit') 
    else:
        sender = User.query.get_or_404(user_id, "Sender does not exist")
        if pin_number == int(sender.pin):
            if amount <= sender.balance:
                receiver = User.query.get_or_404(receiver_id, "Receiver user does not exist")
                sender.balance -= amount
                receiver.balance += amount
                db.session.commit()
                user_schema = UserSchema()
                response = user_schema.dump(receiver).data
                return jsonify(response)
            else:
                abort(400, description='You dont have enought amount of money in your acount!')
        else:
            abort(400, description="Pin is not correct")'''


'''
    pin_number = request.args.get('pin') 
    sender = request.args.get('sender') 
    receiver = request.args.get('receiver') 
    amount = request.args.get('amount') 
    amount = int(amount) 

    senderUser = User.query.filter_by(name=sender).first()
    receiverUser = User.query.filter_by(name=receiver).first()

    if receiverUser and (senderUser.pin == pin_number):
        senderUser.balance -= amount
        receiverUser.balance += amount
        db.session.commit()
        return "The sender's new balance is {} EUR. The receiver's new balance is {} EUR.".format(senderUser.balance, receiverUser.balance)
    else:
        return "The account you want to transfer money to does not exist." '''
#0
@app.route('/users', methods=['GET'])
def get_users():
    user_schema = UserSchema(many=True) #expects a list with all the users (many=True)
    users = User.query.all()
    response = user_schema.dump(users).data
    return  jsonify(response)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json(force=True)
    new_name = data['name']
    new_pin = int(data['pin'])
    new_balance = int(data['balance'])
    if not new_name and new_pin and new_balance:
        abort(400, description="Bad request")
    else:
        # check if user already exists
        user = User.query.filter_by(name=new_name).first()
        if user:
            abort(400, description="User already exists.")
        else:
            new_user = User(name=new_name, pin=new_pin, balance=new_balance)
            db.session.add(new_user)
            db.session.commit()
            user_schema = UserSchema()
            response = user_schema.dump(new_user).data    #to serialize we use Marshmallow library
            return jsonify(response)


# get resource id 1
# GET /users/1

@app.route('/users/<int:user_id>', methods=['GET'])
def user_info(user_id):
    user = User.query.get_or_404(user_id)
    user_schema = UserSchema()   #
    response = user_schema.dump(user).data
    return jsonify(response)
   
# update resource details
# PUT /users/1 ('name' = 'John')
# PUT updates all the information of a resource ≠ PATCH

@app.route('/users/<int:user_id>', methods=['PUT']) # id is unique! name user_id needs to be identical with parameter but can be anything
def update_user(user_id):
    data = request.get_json(force=True)
    new_name = data['name']
    new_balance = data['balance']
    new_pin = data['pin']
    user = User.query.get_or_404(user_id)
    user.name = new_name
    user.pin = new_pin
    user.balance = new_balance
    db.session.commit()
    user_schema = UserSchema()
    response = user_schema.dump(user).data   
    return jsonify(response)

# delete resource selected
# DELETE /users/1

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id, "Bye bye Baby!")
    db.session.delete(user)
    db.session.commit()
    return '', 204

       
       
