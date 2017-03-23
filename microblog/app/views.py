from app import app
from flask import render_template
from datetime import date

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

