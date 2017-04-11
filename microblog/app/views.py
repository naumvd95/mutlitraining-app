from app import app, db, oid, lm
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from models import User, ROLE_USER, ROLE_ADMIN
from datetime import date
from forms import LoginForm
import requests, json

@app.route("/", methods=["GET"])
def get_home():
    #TODO check it, when server replaced into public WEB
    ip = request.environ['REMOTE_ADDR']
    send_url = 'http://freegeoip.net/json/'+ip
    r = requests.get(send_url)
    location_data = json.loads(r.text)
    country = location_data['country_name']
    city = location_data['city']
    print country + ',' + city + send_url + '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1'
    return country + city


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
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
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])

    return render_template('login.html',
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])
@oid.after_login
def after_login(resp):
    location = get_home()
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname = nickname, email = resp.email, role = ROLE_USER, location = location)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
