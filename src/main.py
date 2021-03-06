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
from .models import User, Band, Merchendise, Discography, Blog
from . import db

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# imports used to gather important data locally used for displaying 
from datetime import datetime
import os
from os import listdir
from os.path import isfile, join

main = Blueprint('main', __name__)

######## FORM CLASSES: ########
class SellMerchForm(FlaskForm):
  item_name = StringField('Item Name: ', validators=[DataRequired()])
  quantity = StringField('Quantity: ', validators=[DataRequired()])
  submit = SubmitField('Submit')

class AddMerchForm(FlaskForm):
  item_name = StringField('Item Name: ', validators=[DataRequired()])
  price = StringField('Price: ', validators=[DataRequired()])
  quantity = StringField('Quantity: ', validators=[DataRequired()])
  submit = SubmitField('Submit')

class AddDiscogForm(FlaskForm):
  album = StringField('Album: ', validators=[DataRequired()])
  song = StringField('Song: ', validators=[DataRequired()])
  submit = SubmitField('Submit')

class AddBlogForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired()])
    post = StringField('Post: ', validators=[DataRequired()])
    submit = SubmitField('Submit')

######## ROUTING FUNCTIONS ########
@main.route('/')
def index():
    return render_template('apollo.html')

@main.route('/profile')
def reg_profile():
    return render_template('profile.html', blog=Blog)

@main.route('/profile/<int:uid><int:band>')
def profile(uid, band):
    return render_template('profile.html', blog=Blog)

@main.route('/profile/<int:bid>')
def band_public(bid):
    print(bid)
    # store the band in both user and band format used for output in the display
    band_user = User.query.filter_by(id=int(bid)).first()
    band = Band.query.filter_by(user_id=band_user.id).first()
    # update the number of times the page has been viewed and commit changes
    band.page_views += 1
    db.session.commit()
    return render_template('band-public.html', bid=bid, band=band, band_user=band_user, blog=Blog)

@main.route('/popular-songs', methods=['GET','POST'])
def popular():
    if request.method == 'POST':
        if request.form['like']:
            split = request.form['like'].split('*')
            album = split[0]
            song = split[1]
            discog = Discography.query.filter_by(album=album, song=song).first()
            discog.likes +=1
            db.session.commit()
    return render_template('popular-songs.html', top10_songs=db.session.query(User, Discography).filter(User.id == Discography.user_id).order_by(Discography.likes.desc()).limit(10))

@main.route('/bands')
def bands():
    all_bands = User.query.filter_by(account_type="band")
    # get all the images in the static/images folder, if the band has an image display it
    return render_template('bands.html', all_bands=all_bands, BandQ=Band, 
        top3_bands=db.session.query(User, Band).filter(User.id == Band.user_id).order_by(Band.page_views.desc()).limit(3),
        image_files=[file.split('.')[0] for file in listdir(os.getcwd() + '/src/static/images') if isfile(join(os.getcwd() + '/src/static/images', file))])

@main.route('/signup-login')
def singup_login_redir():
    return render_template('signup-login-redirect.html')

# function that deals with blog posts 
@main.route('/blog', methods=['GET','POST'])
def blog():
    # intialize the blog form
    form = AddBlogForm(email='', post='')
    if form.validate_on_submit():
        # get the user for this email to add their id val to the blog table
        user = User.query.filter_by(email=form.email.data).first()
        # make sure there is a user associated with this account, if so make the post
        if user:
            # get the current date and time
            now = datetime.now().strftime("%d/%m/%Y %H:%M:%S").split()
            date = now[0]
            time = now[1]
            # create a new row in the blog table
            blog_post = Blog(user_id=user.id, date=date, time=time, post=form.post.data)
            # update the database
            db.session.add(blog_post)
            # update the number of times this user has made a post
            user.num_posts += 1
            db.session.commit()
            return redirect(url_for('main.blog'))
        else:
            flash("Please use a registered email!")
            return redirect(url_for('main.blog'))
    # make sure to pass in db.session values used for the blog statistics
    return render_template('blog.html', form=form, num_posts=db.session.query(Blog).count(), 
        unique_users=db.session.query(Blog).distinct(Blog.user_id).group_by(Blog.user_id).count(),
        last_date_entry=str(db.session.query(Blog.date).order_by(Blog.user_id.desc()).first())[2:12],
        last_time_entry=str(db.session.query(Blog.time).order_by(Blog.user_id.desc()).first())[2:10])

# function that "purchases" merch for a user
@main.route('/buy-merch/<int:uid>', methods=['GET','POST'])
def buy_merch(uid):
    # store all the merch for this user id (which is a band)
    all_merch = Merchendise.query.filter_by(user_id=uid)
    # intialize the sell form
    form = SellMerchForm(item_name='', quantity='')
    if form.validate_on_submit():
        # now query for the specific item
        merch = Merchendise.query.filter_by(user_id=uid, item_name=form.item_name.data).first()
        # if that item exits, continue
        if merch:
            # update the quantity (as they purchased) and commit changes
            total_item = merch.quantity
            merch.quantity = merch.quantity - int(form.quantity.data)
            if merch.quantity < 0:
                merch.quantity = 0
                db.session.commit()
                flash("You ordered more than we have in stock. Ordered max amount of " + str(total_item) + " isntead.")
            return render_template('sell-merch.html', form=form, rows=all_merch, bid=uid)
        else:
            flash("That item doesn't exist!")
    return render_template('sell-merch.html',form=form, rows=all_merch, bid=uid)

# function to add merch to the merchendise table (for a band)
@main.route('/add-merch/<int:uid>', methods=['GET','POST'])
def add_merch(uid):
    # initialize the add form
    form = AddMerchForm(item_name='', price='', quantity='')
    if form.validate_on_submit():
        # get the item in the database associated with the input
        merch = Merchendise.query.filter_by(user_id=uid, item_name=form.item_name.data).first()
        # if that item exits, update its values and commit changes
        if merch:
            # update this items 
            merch.price = form.price.data
            merch.quantity += int(form.quantity.data)
            db.session.commit()
        # o/w create a new merch item and commit changes
        else:
            new_merch = Merchendise(user_id=uid, item_name=form.item_name.data, price=form.price.data, quantity=form.quantity.data)
            db.session.add(new_merch)
            db.session.commit()
        return redirect(url_for('main.profile', uid=uid, band=1))
    return render_template('add-merch.html', form=form) 

# function to show the discography for a band
@main.route('/show_discog/<int:bid>', methods=['GET','POST'])
def display_discog(bid):
    # store all the discography elements for the given user id (band)
    if request.method == 'POST':
        if request.form['like']:
            split = request.form['like'].split('*')
            album = split[0]
            song = split[1]
            discog = Discography.query.filter_by(user_id=bid, album=album, song=song).first()
            discog.likes +=1
            db.session.commit()
    all_discography = Discography.query.filter_by(user_id=bid)
    return render_template('display-discography.html',rows=all_discography, bid=bid)

# function to add to a band's discography
@main.route('/add-discog/<int:uid>', methods=['GET','POST'])
def add_discog(uid):
    # initialize the add form
    form = AddDiscogForm(album='', song='')
    if form.validate_on_submit():
        # get the input elements used to create a new element
        discog = Discography.query.filter_by(user_id=uid, album=form.album.data, song=form.song.data).first()
        # add only if the element doesn't exist
        if discog:
            #Error repeat song
            flash("Song already exists!")
        else:
            # create the new element and commit changes 
            new_discog = Discography(user_id=uid, album=form.album.data, song=form.song.data, likes=0)
            db.session.add(new_discog)
            db.session.commit()
        return redirect(url_for('main.profile', uid=uid, band=1))
    return render_template('add-discography.html', form=form, Discography=Discography) 
