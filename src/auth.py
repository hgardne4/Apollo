"""
Team "Birk and Socks:" Henry Gardner, Miller Hickman, and George Gardner
CSC210 Final Project
Prof. Zhupa
Apollo Music Platform

This file is the user login page for the Apollo Music Platform, it handles the redirecting and basic initializations. 

Aid:
https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
"""

# basic flask, SQL, etc. imports
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from .models import User, Band
from . import db

auth = Blueprint('auth', __name__)

# WHEN THE USER GOES TO THE LOGIN PAGE
@auth.route('/login')
def login():
    return render_template('login.html')

# WHEN THE USER GOES TO THE SIGNUP PAGE
@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
	# get the user input
	email = request.form.get('email')
	password = request.form.get('password')
	name = request.form.get('name')
	account_type = request.form.get('account_type')

	# check if the account that is signing up is a user or band and complete corresponding actions
	if account_type.lower() == 'user':
		# attempt to grab the data provided in the database 
		user = User.query.filter_by(email=email).first()
		# if the data does exist (non-empty) then output to user that the email already exists
		if user:
			flash('Email already exists')
			return redirect(url_for('auth.signup'))

		# if the email does not already exist, then create a new user 
		new_user = User(name=name, email=email, password=generate_password_hash(password, method='sha256'), num_logins=0)
		
		# add the new user to the database
		db.session.add(new_user)
		db.session.commit()
		return redirect(url_for('auth.login'))
	elif account_type.lower() == 'band':
		# attempt to grab the data provided in the database 
		band = Band.query.filter_by(email=email).first()
		# if the data does exist (non-empty) then output to user that the email already exists
		if band:
			flash('Email already exists')
			return redirect(url_for('auth.signup'))

		# if the email does not already exist, then create a new user 
		new_band = Band(name=name, email=email, password=generate_password_hash(password, method='sha256'), num_logins=0)
		
		# add the new user to the database
		db.session.add(new_band)
		db.session.commit()
		return redirect(url_for('auth.login'))
	else:
		flash('Unrecognized account type')
		return redirect(url_for('auth.signup'))

@auth.route('/login', methods=['POST'])
def login_post():
	# get the email, password, and name from the user input
    email = request.form.get('email')
    password = request.form.get('password')

    # get the user/band data from the database
    user = User.query.filter_by(email=email).first()
    band = Band.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
    	user.num_logins += 1
    	db.session.commit()
    	login_user(user)
    elif band and check_password_hash(band.password, password):
    	band.num_logins += 1
    	db.session.commit()
    	login_user(band)
    else:
    	flash('Unrecognized account details, please check your login details and try again.')
    	return redirect(url_for('auth.login'))
    return redirect(url_for('main.profile'))