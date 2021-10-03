from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email

class FitbitUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    api_key = PasswordField('Apikey', validators=[DataRequired()])
    api_secret_key = PasswordField('Apisecretkey', validators=[DataRequired()])
    submit = SubmitField('Add User')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')