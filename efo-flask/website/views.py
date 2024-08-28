from flask import Blueprint, render_template, send_from_directory, flash, redirect, request  # Import the Blueprint class and the render_template function
from .models import Cars, Cart
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)  # Create a Blueprint object called views

@views.route('/media/<path:filename>')
def get_media(filename):
    return send_from_directory('../media', filename)

@views.route('/')  # Create a route decorator for the / URL
def home():
    
    cars = Cars.query.filter_by(discount_sale=True)



    return render_template("home.html", cars=cars)


@views.route('/car/<int:id>')  # Create a route decorator for the /car/<id> URL
def car(id):
    car = Cars.query.get(id)
    return render_template("car.html", car=car)


@views.route('/add-to-cart/<int:id>')  # Create a route decorator for the /add-to-cart/<id> URL
@login_required
def add_to_cart(id):
    car = Cars.query.get(id)
    car_exists = Cart.query.filter_by(car_id=id, user_id=current_user.id).first()

    if car_exists:
        try:
            car_exists.quantity += 1
            db.session.commit()
            flash('Item added to cart')
            return request.referrer
        except Exception as e:
            print(e)
            return redirect(request.referrer)
    else:
        try:
            new_cart_item = Cart()
            new_cart_item.quantity = 1
            new_cart_item.user_id = current_user.id
            new_cart_item.car_id = id

            db.session.add(new_cart_item)
            db.session.commit()
        except Exception as e:
            print(e)

    return render_template("add_to_cart.html", car=car)

