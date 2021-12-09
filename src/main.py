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
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('apollo.html')

@main.route('/profile')
def profile():
    return render_template('profile.html')

@main.route('/genres')
def genres():
    return render_template('genres.html')

@main.route('/popular-songs')
def popular():
    return render_template('popular-songs.html')

@main.route('/bands')
def bands():
    return render_template('bands.html')

@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/signup')
def signup():
    return render_template('signup.html')

@main.route('/blog')
def blog():
    return render_template('blog.html')
