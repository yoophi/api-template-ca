from datetime import datetime

from .database import db


class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column('id', db.Integer, primary_key=True)
    email = db.Column('email', db.Unicode)
    name = db.Column('name', db.Unicode)
    created_at = db.Column('created_at', db.DateTime, default=datetime.utcnow)
