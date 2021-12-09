"""
Team "Birk and Socks:" Henry Gardner, Miller Hickman, and George Gardner
CSC210 Final Project
Prof. Zhupa
Apollo Music Platform

This file is the user login page for the Apollo Music Platform, it handles the redirecting and basic initializations. 

Aid:
https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
"""

# basic imports needed for flask, initializing the SQL DB, etc
from flask import Blueprint, render_template
from .models import User, Band, Merchendise 
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('apollo.html')

@main.route('/profile/<int:uid><int:band>')
def profile(uid, band):
    curr = ""
    if band == 1:
        curr = Band.query.filter_by(id=uid).first()
    else:
        curr = User.query.filter_by(id=uid).first()
    return render_template('profile.html', user=curr)

@main.route('/genres')
def genres():
    return render_template('genres.html')

@main.route('/popular-songs')
def popular():
    return render_template('popular-songs.html')

@main.route('/bands')
def bands():
    return render_template('bands.html')

@main.route('/signup-login')
def singup_login_redir():
    return render_template('signup-login-redirect.html')

# @main.route('/login')
# def login():
#     return render_template('login.html')

# @main.route('/signup')
# def signup():
#     return render_template('signup.html')

@main.route('/blog')
def blog():
    return render_template('blog.html')
