"""
Team "Birk and Socks:" Henry Gardner, Miller Hickman, and George Gardner
CSC210 Final Project
Prof. Zhupa
Apollo Music Platform

This file is creates a user class for the Apollo Music Platform.

Aid:
https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

OBJECTS THAT REFERENCE THE TABLES IN THE DATABASE:

Current Tables:
    - User
    - Band
    - Merchendise
    - Discography
    - Blog
"""

# basic flask and SQL imports
from flask_login import UserMixin
from . import db

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
    num_posts = db.Column(db.Integer)

# BAND TABLE
class Band(db.Model):
    __tablename__ = 'band'
    # initialize the primary key in the SQL Database to be the id
    id = db.Column(db.Integer, primary_key=True)
    # Band CONTENTS STORED
    user_id = db.Column(db.Integer)
    genre = db.Column(db.String(100))
    page_views = db.Column(db.Integer)

# MERCHENDISE TABLE
class Merchendise(db.Model):
    __tablename__ = 'merchendise'
    # initialize the primary key in the SQL Database to be the id
    id = db.Column(db.Integer, primary_key=True)
    # MERCHENDISE CONTENTS STORED:
    user_id = db.Column(db.Integer)
    item_name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

# DISCOGRAPHY TABLE
class Discography(db.Model):
    __tablename__ = 'discography'
    # initialize the primary key in the SQL Database to be the id
    id = db.Column(db.Integer, primary_key=True)
    # DISCOGRAPHY CONTENTS STORED:
    user_id = db.Column(db.Integer)
    album = db.Column(db.String(100))
    song = db.Column(db.String(100))

# BLOG TABLE
class Blog(db.Model):
    __tablename__ = 'blog'
    # initialize the primary key in the SQL Database to be the id
    id = db.Column(db.Integer, primary_key=True)
    # BLOG CONTENTS STORED:
    user_id = db.Column(db.Integer)
    date = db.Column(db.String(100))
    time = db.Column(db.String(100))
    post = db.Column(db.String(300))