from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    password_check=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember_me=BooleanField('Remember Me')
    submit=SubmitField('Login')

class SearchForm(FlaskForm):
    country=StringField('Username',validators=[DataRequired()])