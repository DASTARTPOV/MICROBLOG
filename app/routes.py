from app import app
from flask import render_template

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