from flask import Blueprint, render_template, flash, redirect  # Import the Blueprint class 
from .forms import signup_form, login_form, changePassword  # Import the signup_form and login_form classes from the forms.py file
from .models import User  # Import the User class from the models.py file
from . import db
from flask_login import login_user, login_required, logout_user


auth = Blueprint('auth', __name__)  # Create a Blueprint object called views


@auth.route('/login', methods=['GET', 'POST'] )  # Create a route decorator for the /login URL
def login():
    form = login_form()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user:
            if user.check_password(password):
                flash('Logged in successfully!')
                login_user(user)
                return redirect('/')
            
            else:
                flash('Incorrect password')
        else:
            flash('User does not exist')
        
    return render_template("login.html", form=form)
    

@auth.route('/sign-up', methods=['GET', 'POST'])  # Create a route decorator for the /sign-up URL
def sign_up():
    form = signup_form()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password1 = form.password1.data
        password2 = form.password2.data

        if password1 == password2:
            new_user = User()
            new_user.email = email
            new_user.username = username
            new_user.password = password2
            
            try:
                db.session.add(new_user)
                db.session.commit()
                flash('User created successfully. You can Login now', 'success')
                return redirect(('/login'))
            except Exception as e:
                print(e)
                flash('User already exists')
                return redirect(('/sign-up'))
            
            form.email.data = ''
            form.username.data = ''
            form.password1.data = ''
            form.password2.data = ''

        return redirect(('/sign-up'))


    return render_template("signup.html", form=form)


@auth.route('/logout', methods=['GET', 'POST'])  # Create a route decorator for the /logout URL
@login_required
def logout():
    logout_user()
    return redirect('/')


@auth.route('/profile/<int:user_id>')  # Create a route decorator for the /profile URL
@login_required
def profile(user_id):
    user = User.query.get(user_id)
    return render_template('profile.html', user=user)


@auth.route('/change-password/<int:user_id>', methods=['GET', 'POST'])  # Create a route decorator for the /change-password URL
@login_required
def change_password(user_id):
    form = changePassword()
    user_id = User.query.get(user_id)
    if form.validate_on_submit():
        old_password = form.old_password.data
        new_password = form.new_password1.data
        new_password2 = form.new_password2.data

        if user_id.check_password(old_password):
            if new_password == new_password2:
              user_id.password = new_password2
              db.session.commit()
              flash('Password changed successfully')
              return redirect('/profile')
            else:
              flash('Passwords do not match')
              return redirect('/change-password')
        else:
            flash('Incorrect Password')
            return redirect('/change-password')
    return render_template('changePassword.html', form=form)