from . import db
from flask_login import UserMixin

class Info(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    productInfo =  db.Column(db.String(1000))
    numOfProd = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    address = db.Column(db.String(250))
