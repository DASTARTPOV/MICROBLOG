from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm
from flask import flash, redirect

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
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"{form.username.data}Sign In successfully")
        return redirect('/index')
    return render_template('login.html', title='LogIn', form=form)