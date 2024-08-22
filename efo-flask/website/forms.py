from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, EmailField, TextAreaField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError



class signup_form(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=15)])
    password1 = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40)])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField('Sign Up')

class login_form(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')