from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True),
    email = db.Column(db.String(64), index=True, unique=True),
    password_hash = db.Column(db.String(64))

    def __repr__(self):
        return '<User {}>'.format(self.email)
    
class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True),
    asset_name = db.Column(db.String(64)),
    location = db.Column(db.String(64)),
    updated = db.Column(db.String(10))

    def __repr__(self):
        return '<User {}>'.format(self.email)