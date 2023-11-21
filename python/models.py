from datetime import datetime
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class UserInfo(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.String(100), primary_key=True)
    item_id = db.Column(db.String(100))
    account = db.relationship('Account', backref='user_info')


# http://localhost:3000/api/accounts
class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(50))
    currency = db.Column(db.String(5))
    balance = db.Column(db.Integer)
    acc_type = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'currency': self.currency,
            'balance': self.balance,
            'acc_type': self.acc_type,
            'user_id': self.user_id
        }


# http://localhost:3000/api/transactions
class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(50))
    category = db.Column(db.String(50))
    amount = db.Column(db.Integer)
    logo_url = db.Column(db.String(100))
    website = db.Column(db.String(100))
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'amount': self.amount,
            'logo_url': self.logo_url,
            'website': self.website,
            'account_id': self.account_id
        }

