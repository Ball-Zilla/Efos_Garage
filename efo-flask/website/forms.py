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


class add_car(FlaskForm):
    make = StringField('Make', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    current_price = StringField('Current Price', validators=[DataRequired()])
    previous_price = StringField('Previous Price', validators=[DataRequired()])
    in_stock = BooleanField('In Stock')
    product_image = StringField('Product Image', validators=[DataRequired()])
    discount_sale = BooleanField('Discount Sale')
    submit = SubmitField('Add Car')

class changePassword(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    new_password1 = PasswordField('New Password', validators=[DataRequired()])
    new_password2 = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password1')])
    submit = SubmitField('Change Password')