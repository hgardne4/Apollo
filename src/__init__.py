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
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# initialize our database and pass this to the other files
db = SQLAlchemy()

def create_app():
    # initialize our flask app
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # initalize the login manager which helps connect to the flask-login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # NOTE:
    # A User is either a fan OR a band
    from .models import User
    @login_manager.user_loader
    def load_user(id):
        if User.query.get(int(id)):
            return User.query.get(int(id))

    # APPEND ALL THE TABLES WITH THE CREATE_ALL() FUNCTION:
    # NOTE: need to wrap in the app_context() and commit changes
    with app.app_context():
        db.create_all()
        db.session.commit()
    
    # return our flask app
    return app