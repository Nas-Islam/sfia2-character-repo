from application import app, db
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    item = db.Column(db.String(50), nullable=False)
    class_type = db.Column(db.String(50), nullable=False)
    bonus = db.Column(db.String(400), nullable=False)