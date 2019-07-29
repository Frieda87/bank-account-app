from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///side.db' 
db = SQLAlchemy(app)
ma = Marshmallow(app)

from crazyshit import routes