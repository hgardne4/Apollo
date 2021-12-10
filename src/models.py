"""
Team "Birk and Socks:" Henry Gardner, Miller Hickman, and George Gardner
CSC210 Final Project
Prof. Zhupa
Apollo Music Platform

This file is creates a user class for the Apollo Music Platform.

Aid:
https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
"""

# basic flask and SQL imports
from flask_login import UserMixin
from . import db

"""
OBJECTS THAT REFERENCE THE TABLES IN THE DATABASE:
"""

# USER TABLE
class User(UserMixin, db.Model):
    __tablename__ = 'user'

    # initialize the primary key in the SQL Database to be the id
    id = db.Column(db.Integer, primary_key=True)
    # USER CONTENTES STORES:
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    account_type = db.Column(db.String(100))
    num_logins = db.Column(db.Integer)


# BAND TABLE
class Band(UserMixin, db.Model):
    __tablename__ = 'band'

    # initialize the primary key in the SQL Database to be the id
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    #account_id = db.Column(db.Integer, db.ForeignKey='user.id')
    #account = relationship('Parent', back_populates='children')

    # Band CONTENTS STORED
    genre = db.Column(db.String(100))
    page_views = db.Column(db.Integer)

# MERCHENDISE TABLE
class Merchendise(db.Model):
    __tablename__ = 'merchendise'

    # initialize the primary key in the SQL Database to be the id
    id = db.Column(db.Integer, primary_key=True)
    #band_id = db.Column(db.Integer, ForeignKey='band.id')
    #band = relationship('Parent', back_populates='children')
    # MERCHENDISE CONTENTS STORED:
    item_name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)