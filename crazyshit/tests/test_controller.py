from crazyshit import app, db
from crazyshit.models import User
import unittest
import json

class TestController(unittest.TestCase):

    def setUp(self):
        app.config['TESTING']=True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' 
        app.config['DEBUG']=False
        db.drop_all()
        db.create_all()
        self.app = app.test_client()
    
    def tearDown(self):
        pass

    def create_user(self):
        user = User(name='Test User', pin=1234, balance=2000, id=1)
        db.session.add(user)
        db.session.commit()
        return user
    
    def create_second_user(self):
        user_2 = User(name='Test User2', pin=3333, balance=3000, id=2)
        db.session.add(user_2)
        db.session.commit()
        return user_2

    def create_user_by_param(self, name, pin, balance):
        user = User(name=name,pin=pin,balance=balance)
        db.session.add(user)
        db.session.commit()
        return user

    def get_user_by_id(self, id):
        return User.query.filter_by(id=id).first()

    def test_create_user(self):
        mock_request_data = {
            'name': 'Test User',
            'pin': '1234',
            'balance': 1000
        }
        response = self.app.post('/users', data=json.dumps(mock_request_data))
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code,200)
        self.assertEqual(data['name'], 'Test User')
        self.assertEqual(data['pin'], 1234)
        self.assertEqual(data['balance'], 1000)

    def test_get_users(self):
        mock_user = self.create_user()
        response = self.app.get('/users')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code,200)
        self.assertEqual(data[0]['name'], mock_user.name)
        self.assertEqual(data[0]['pin'], mock_user.pin)
        self.assertEqual(data[0]['balance'], mock_user.balance)

    def test_delete_user(self):
        mock_user = self.create_user()
        response = self.app.delete(f'/users/{mock_user.id}')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code,204)
        self.assertEqual(data,'')
        user = self.get_user_by_id(mock_user.id)
        self.assertIsNone(user)
    
    def test_get_user_by_id_404(self):
        mock_user = self.create_user()
        response = self.app.get(f'/users/{mock_user.id+1}')
        self.assertEqual(response.status_code, 404)

    def test_update_user(self):
        mock_update_data = {
            'name': 'Updated User',
            'pin': 1239,
            'balance': 2000
        }
        mock_user = self.create_user()
        response = self.app.put(f'/users/{mock_user.id}', data=json.dumps(mock_update_data))
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code,200)
        self.assertEqual(data['name'], 'Updated User')
        self.assertEqual(data['pin'], 1239)
        self.assertEqual(data['balance'], 2000)
    
    def test_transfer_money(self):
        mock_amount_transfer = {
            'amount': 35,
            'pin': 1234,
            'receiver_id': 2
        }
        mock_sender = self.create_user()
        mock_receiver = self.create_second_user() #or mock_receiver = self.create_user_by_param(name="Test Receiver",pin='1235',balance=500)
        response = self.app.patch(f'/users/{mock_sender.id}/transfer', data=json.dumps(mock_amount_transfer))
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data[1]['name'], 'Test User2')
        self.assertEqual(data[1]['balance'], 3035)
        self.assertEqual(data[0]['name'], mock_sender.name)
        self.assertEqual(data[0]['balance'], 1965)
        self.assertEqual(data[0]['pin'], mock_sender.pin)

    def test_withdraw_money(self):
        mock_user_data = {
            'amount': 40,
            'pin': 1234
        }
        mock_user = self.create_user()
        response = self.app.patch(f'/users/{mock_user.id}/withdraw', data=json.dumps(mock_user_data))
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['balance'], 1960)
        self.assertEqual(data['pin'], mock_user.pin)
        self.assertEqual(response.status_code,200)
    
    def test_withdrawl_too_big(self):
        mock_user_data = {
            'amount': 40,
        }
        mock_user = self.create_user()
        response = self.app.patch(f'/users/{mock_user.id}/withdraw')
        self.assertEqual(response.status_code,400)
        
    def test_receiver_money_transfer_not_existent(self):
        mock_amount_transfer = {
            'amount': 35,
            'pin': 1234,
            'receiver_id': 3
        }
        mock_sender = self.create_user()
        mock_receiver = self.create_second_user() 
        response = self.app.patch(f'/users/{mock_sender.id}/transfer', data=json.dumps(mock_amount_transfer))
        self.assertEqual(response.status_code,404)


