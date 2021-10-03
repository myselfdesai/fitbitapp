from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email

class FitbitUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    client_id = StringField('Client id', validators=[DataRequired()])
    client_secret_key = StringField('Cleint secret key', validators=[DataRequired()])
    access_token = StringField('Access Token', validators=[DataRequired()])
    refresh_token = StringField('Refresh Token', validators=[DataRequired()])
    submit = SubmitField('User')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')