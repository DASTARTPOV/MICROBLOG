from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from flask import flash, redirect
from app.models import User
from flask_login import current_user, login_user

@app.route('/')
@app.route('/index')
def index():
    user = {"username":"Artemy"}
    posts = [
        {
            'author': {'username': 'Bogdan Evtushenco'},
            'body': 'Zdorovo!!!'
        },
        {
            'author': {'username': 'Alexandr Lukin'},
            'body': 'HEllO BOGDANCHYC'
        },
        {
            'author': {'username': 'Bogdan Evtushenco'},
            'body': 'A ТЫ ТУТ ОТКУДА ???'
        }

    ]

    return render_template("index.html", title='houme', user=user, posts = posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in')
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        flash(f"{form.username.data}  Sign In successfully")
        return redirect(url_for('index'))
    return render_template('login.html', title='LogIn', form=form)