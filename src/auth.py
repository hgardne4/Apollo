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

from datetime import datetime

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

class BlogForm(FlaskForm):
  email = StringField('Email: ', validators=[DataRequired()])
  post = StringField('Post: ', validators=[DataRequired()])
  submit = SubmitField('Submit')

# WHEN THE USER SIGNS UP
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

		new_user = User(name=form.name.data, email=form.email.data, password=generate_password_hash(form.password.data, method='sha256'), account_type="user", num_logins=0, num_posts=0)
		db.session.add(new_user)
		db.session.commit()
		return redirect(url_for('auth.login'))

	return render_template('signup.html', form=form, band=False)

# WHEN THE BAND SIGNS UP
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

		# UPDATE THE USER TABLE
		new_user = User(name=form.name.data, email=form.email.data, password=generate_password_hash(form.password.data, method='sha256'), account_type="band", num_logins=0, num_posts=0)
		db.session.add(new_user)
		db.session.commit()

		# UPDATE THE BAND TABLE
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
			login_user(user)
		# o/w output error and redirect to login page
		else:
			flash('Unrecognized account details, please check your login details and try again')
			return redirect(url_for('auth.login'))
    	# if successfully logged in, then redirect to profile page
		return redirect(url_for('main.profile', uid=int(user.id), band=0))

	return render_template('login.html', form=form)