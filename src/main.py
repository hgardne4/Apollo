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
from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import User, Band, Merchendise, Discography
from . import db

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('apollo.html')

@main.route('/profile/<int:uid><int:band>')
def profile(uid, band):
    return render_template('profile.html')

@main.route('/profile/<int:bid>')
def band_public(bid):
    band_to_disp = User.query.filter_by(account_type="band", id=bid).first()
    return render_template('band-public.html', bid=bid, disp_band=band_to_disp)

@main.route('/genres')
def genres():
    return render_template('genres.html')

@main.route('/popular-songs')
def popular():
    return render_template('popular-songs.html')

@main.route('/bands')
def bands():
    all_bands = User.query.filter_by(account_type="band")
    return render_template('bands.html', all_bands=all_bands, BandQ=Band)

@main.route('/signup-login')
def singup_login_redir():
    return render_template('signup-login-redirect.html')

@main.route('/blog')
def blog():
    return render_template('blog.html')

class SellMerchForm(FlaskForm):
  item_name = StringField('Item Name: ', validators=[DataRequired()])
  quantity = StringField('Quantity: ', validators=[DataRequired()])
  submit = SubmitField('Submit')



@main.route('/buy-merch/<int:uid>', methods=[ 'GET' , 'POST' ])
def buy_merch(uid):
    all_merch = Merchendise.query.filter_by(user_id=uid)

    item_name = ' '
    quantity = ' '
    form = SellMerchForm(item_name='', quantity='')

    if form.validate_on_submit():
        merch = Merchendise.query.filter_by(user_id=uid, item_name=form.item_name.data).first()

        if merch:
            
            merch.quantity = merch.quantity - int(form.quantity.data)
            db.session.commit()
            all_merch = Merchendise.query.filter_by(user_id=uid)
            #CHECK FOR LESS THAN 0
            return render_template('sell-merch.html',form=form, rows=all_merch, bid=uid)
        else:
            # MERCH DOES NOT EXIST
            two = 2
    return render_template('sell-merch.html',form=form, rows=all_merch, bid=uid)

class AddMerchForm(FlaskForm):
  item_name = StringField('Item Name: ', validators=[DataRequired()])
  price = StringField('Price: ', validators=[DataRequired()])
  quantity = StringField('Quantity: ', validators=[DataRequired()])
  submit = SubmitField('Submit')

@main.route('/add-merch/<int:uid>', methods=[ 'GET' , 'POST' ])
def add_merch(uid):
    item_name = ' '
    price = ' '
    quantity = ' '
    form = AddMerchForm(item_name='', price='', quantity='')

    if form.validate_on_submit():
        merch = Merchendise.query.filter_by(user_id=uid, item_name=form.item_name.data).first()

        if merch:
            merch.price = form.price.data
            merch.quantity += form.quantity.data
            db.session.commit()
        else:
            new_merch = Merchendise(user_id=uid, item_name=form.item_name.data, price=form.price.data, quantity=form.quantity.data)
            db.session.add(new_merch)
            db.session.commit()
        
        return redirect(url_for('main.profile', uid=uid, band=1))


    return render_template('add-merch.html', form=form) 

class AddMerchForm(FlaskForm):
  item_name = StringField('Item Name: ', validators=[DataRequired()])
  price = StringField('Price: ', validators=[DataRequired()])
  quantity = StringField('Quantity: ', validators=[DataRequired()])
  submit = SubmitField('Submit')

@main.route('/show_discog/<int:bid>', methods=[ 'GET' , 'POST' ])
def display_discog(bid):
    all_discography = Discography.query.filter_by(user_id=bid)
    return render_template('display-discography.html',rows=all_discography, bid=bid)

class AddDiscogForm(FlaskForm):
  album = StringField('Album: ', validators=[DataRequired()])
  song = StringField('Song: ', validators=[DataRequired()])
  submit = SubmitField('Submit')

@main.route('/add-discog/<int:uid>', methods=[ 'GET' , 'POST' ])
def add_discog(uid):
    album = ' '
    song = ' '
    form = AddDiscogForm(album='', song='')

    if form.validate_on_submit():
        discog = Discography.query.filter_by(user_id=uid, album=form.album.data, song=form.song.data).first()

        if discog:
            #Error repeat song
            one = 1
        else:
            new_discog = Discography(user_id=uid, album=form.album.data, song=form.song.data)
            db.session.add(new_discog)
            db.session.commit()
        
        return redirect(url_for('main.profile', uid=uid, band=1))


    return render_template('add-discography.html', form=form) 




