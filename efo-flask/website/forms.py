from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, EmailField, FileField, IntegerField, DecimalField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from flask_wtf.file import FileAllowed



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


class add_car_form(FlaskForm):
    name = StringField('Name of Car', validators=[DataRequired()])
    exterior_color = StringField('Exterior Color', validators=[DataRequired()])
    interior_color = StringField('Interior Color', validators=[DataRequired()])
    engine = StringField('Engine', validators=[DataRequired()])
    transmission = StringField('Transmission Type', validators=[DataRequired()])
    fuel_type = StringField('Fuel Type', validators=[DataRequired()])
    vin_number = IntegerField('VIN Number', validators=[DataRequired()])
    mileage = IntegerField('Mileage', validators=[DataRequired()])
    # make = StringField('Make', validators=[DataRequired()])
    # model = StringField('Model', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    current_price = DecimalField('Current Price', validators=[DataRequired()])
    previous_price = DecimalField('Previous Price', validators=[DataRequired()])
    in_stock = BooleanField('In Stock')
    product_image = FileField('Product Picture', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    discount_sale = BooleanField('Discount Sale')
    submit = SubmitField('Add Car')

class changePassword(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    new_password1 = PasswordField('New Password', validators=[DataRequired()])
    new_password2 = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password1')])
    submit = SubmitField('Change Password')