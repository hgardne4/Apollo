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

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# import all the object and table classes from the models file
from .models import User, Band, Merchendise 
from . import db

auth = Blueprint('auth', __name__)


class NewUserForm(FlaskForm):
  name = StringField('Name: ', validators=[DataRequired()])
  password = StringField('Password: ', validators=[DataRequired()])
  email = StringField('Email: ', validators=[DataRequired()])
  submit = SubmitField('Submit')

class UserLoginForm(FlaskForm):
  password = StringField('Password: ', validators=[DataRequired()])
  email = StringField('Email: ', validators=[DataRequired()])
  submit = SubmitField('Submit')

class BandLoginForm(FlaskForm):
  password = StringField('Password: ', validators=[DataRequired()])
  email = StringField('Email: ', validators=[DataRequired()])
  submit = SubmitField('Submit')

class NewBandForm(FlaskForm):
  name = StringField('Name: ', validators=[DataRequired()])
  password = StringField('Password: ', validators=[DataRequired()])
  email = StringField('Email: ', validators=[DataRequired()])
  genre = StringField('Genre: ', validators=[DataRequired()])
  submit = SubmitField('Submit')

# WHEN THE USER GOES TO THE LOGIN PAGE
# @auth.route('/login')
# def login():
#     return render_template('login.html')

# WHEN THE USER GOES TO THE SIGNUP PAGE
# @auth.route('/signup')
# def signup():
#     return render_template('signup.html')

# @auth.route('/signup', methods=['POST'])
# def signup_post():
# 	# get the user input
# 	email = request.form.get('email')
# 	password = request.form.get('password')
# 	name = request.form.get('name')
# 	account_type = request.form.get('account_type')

# 	# check if the account that is signing up is a user or band and complete corresponding actions
# 	if account_type.lower() == 'user' or account_type.lower() == 'band':
# 		# attempt to grab the data provided in the database 
# 		user = User.query.filter_by(email=email).first()
# 		# if the data does exist (non-empty) then output to user that the email already exists
# 		if user:
# 			flash('Email already exists')
# 			return redirect(url_for('auth.signup'))

# 		# if the email does not already exist, then create a new user 
# 		new_user = User(name=name, email=email, password=generate_password_hash(password, method='sha256'), account_type=account_type.lower(), num_logins=0)
		
# 		# add the new user to the database
# 		db.session.add(new_user)
# 		db.session.commit()
# 		return redirect(url_for('auth.login'))
# 	else:
# 		flash('Unrecognized account type')
# 		return redirect(url_for('auth.signup'))


# @auth.route('/login', methods=['POST'])
# def login_post():
# 	# get the email, password, and name from the user input
#     email = request.form.get('email')
#     password = request.form.get('password')

#     # get the user/band data from the database
#     user = User.query.filter_by(email=email).first()

#     # check if this is a user and the password matches, if so log them in
#     if user and check_password_hash(user.password, password):
#     	user.num_logins += 1
#     	db.session.commit()
#     	login_user(user)
#  	# o/w output error and redirect to login page
#     else:
#     	flash('Unrecognized account details, please check your login details and try again.')
#     	return redirect(url_for('auth.login'))
#     # if successfully logged in, then redirect to profile page
#     return redirect(url_for('main.profile'))



@auth.route('/signup/user', methods=['GET', 'POST'])
def signup_user():
	name = ' '
	password = ''
	email = ' '
	form = NewUserForm(name='', password='', email='')
    	
	if form.validate_on_submit():
		# if the email does not already exist, then create a new user 
		user = User.query.filter_by(email=form.email.data).first()
		if user:
			flash('Email already exists')
			return redirect(url_for('auth.signup_user'))

		new_user = User(name=form.name.data, email=form.email.data, password=generate_password_hash(form.password.data, method='sha256'), account_type="user", num_logins=0)
		db.session.add(new_user)
		db.session.commit()
		return redirect(url_for('auth.login'))

	return render_template('signup.html', form=form, band=False)




@auth.route('/signup/band', methods=['GET', 'POST'])
def signup_band():
	name = ''
	password = ''
	email = ''
	genre = ''
	form = NewBandForm(name='', password='', email='', genre='')
    	
	if form.validate_on_submit():
		# if the email does not already exist, then create a new user 
		band = User.query.filter_by(email=form.email.data).first()
		if band:
			flash('Email already exists')
			return redirect(url_for('auth.signup_band'))
		new_user = User(name=form.name.data, email=form.email.data, password=generate_password_hash(form.password.data, method='sha256'), account_type="band", num_logins=0)
		db.session.add(new_user)
		db.session.commit()

		
		new_band = Band(user_id=int(new_user.id), genre=form.genre.data, page_views=0)
		db.session.add(new_band)
		db.session.commit()
		return redirect(url_for('auth.login'))

	return render_template('signup.html', form=form, band=True)



@auth.route('/login', methods=['GET', 'POST'])
def login():
	# get the email, password, and name from the user input

	password = ''
	email = ''
	form = UserLoginForm(password='', email='')

	if form.validate_on_submit():
		# get the user/band data from the database
		user = User.query.filter_by(email=form.email.data).first()

		# check if this is a user and the password matches, if so log them in
		if user and check_password_hash(user.password, str(form.password.data)):
			user.num_logins += 1
			db.session.commit()
			#login_user(user)
		# o/w output error and redirect to login page
		else:
			flash('Unrecognized account details, please check your login details and try again.')
			return redirect(url_for('auth.login'))
    	# if successfully logged in, then redirect to profile page
		id = int(user.id)
		return redirect(url_for('main.profile', uid=id, band=0))

	return render_template('login.html', form=form)


# @auth.route('/login/user', methods=['GET', 'POST'])
# def login_user():
# 	# get the email, password, and name from the user input

# 	password = ''
# 	email = ''
# 	form = UserLoginForm(password='', email='')

# 	if form.validate_on_submit():
# 		# get the user/band data from the database
# 		user = User.query.filter_by(email=form.email.data).first()

# 		# check if this is a user and the password matches, if so log them in
# 		if user and check_password_hash(user.password, str(form.password.data)):
# 			user.num_logins += 1
# 			db.session.commit()
# 			#login_user(user)
# 		# o/w output error and redirect to login page
# 		else:
# 			flash('Unrecognized account details, please check your login details and try again.')
# 			return redirect(url_for('auth.login_user'))
#     	# if successfully logged in, then redirect to profile page
# 		id = int(user.id)
# 		return redirect(url_for('main.profile', uid=id, band=0))

# 	return render_template('login.html', form=form)


# @auth.route('/login/band', methods=['GET', 'POST'])
# def login_band():
# 	# get the email, password, and name from the user input

# 	password = ''
# 	email = ' '
# 	form = BandLoginForm(password='', email='')

# 	if form.validate_on_submit():
# 		# get the user/band data from the database
# 		band = Band.query.filter_by(email=form.email.data).first()

# 		# check if this is a user and the password matches, if so log them in
# 		if band and check_password_hash(band.password, str(form.password.data)):
# 			# user.num_logins += 1
# 			# db.session.commit()
# 			#login_user(user)
# 			id = int(band.id)
# 			return redirect(url_for('main.profile', uid=id, band=1))
# 		# o/w output error and redirect to login page
# 		else:
# 			flash('Unrecognized account details, please check your login details and try again.')
# 			return redirect(url_for('auth.login_band'))
#     	# if successfully logged in, then redirect to profile page
# 		id = int(band.id)
# 		return redirect(url_for('main.profile', uid=id, band=1))

# 	return render_template('login.html', form=form)