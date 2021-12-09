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

Current Tables:
    - User login
    - Band login
    - Merch
"""

# USER TABLE
class User(UserMixin, db.Model):
    __tablename__ = 'user'
	# initialize the primary key in the SQL Database to be the id
    id = db.Column(db.Integer, primary_key=True)
    # store the email, password, and names as columns with string contents
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    num_logins = db.Column(db.Integer)


# BAND TABLE
class Band(UserMixin, db.Model):
    __tablename__ = 'band'
    # initialize the primary key in the SQL Database to be the id
    id = db.Column(db.Integer, primary_key=True)
    # store the email, password, and names as columns with string contents
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    num_logins = db.Column(db.Integer)



