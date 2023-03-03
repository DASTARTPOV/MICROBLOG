from flask_wtf import Flask
from wtforms import StringField, PasswordField, SubmitField, BoolingField
from wtforms.validators import DataRequired
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    renember_me = BoolingField('Renember me')
    subnit = SubmitField('Sign In')