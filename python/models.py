from datetime import datetime
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class UserInfo(db.Model):
    __tablename__ = 'user_info'
    access_token = db.Column(db.String(100), primary_key=True)
    item_id = db.Column(db.String(100))
    account = db.relationship('Account', backref='user_info')

class Account(db.Model):
    __tablename__ = 'account'
    
