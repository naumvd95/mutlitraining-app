from app import app
from flask import render_template, flash, redirect
from datetime import date
from forms import LoginForm

@app.route('/')
@app.route('/index')

def index():
    user = { 'nickname': 'vnaumov' } # default user
    posts = [ # post list
        { 
            'author': { 'nickname': 'rkhozinov' }, 
            'body': 'need to change each step from this guide and customize it',
            'timestamp': (date.today()).strftime("%A %d. %B %Y")
        },
        { 
            'author': { 'nickname': 'vkuspits' }, 
            'body': 'agree with @rkhozinov opinion. U get more experience',
            'timestamp': (date.today()).strftime("%A %d. %B %Y")
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])
