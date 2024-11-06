from flask import Blueprint, render_template, send_from_directory, flash, redirect, request  # Import the Blueprint class and the render_template function
from .models import Cars, Cart
from flask_login import login_required, current_user
from . import db
from sqlalchemy.orm import joinedload

views = Blueprint('views', __name__)  # Create a Blueprint object called views

@views.route('/media/<path:filename>')
def get_media(filename):
    return send_from_directory('../media', filename)

@views.route('/')  # Create a route decorator for the / URL
def home():
    
    cars = Cars.query.filter_by(discount_sale=True)



    return render_template("home.html", cars=cars, cart = Cart.query.filter_by(user_id=current_user.id).all()
                           if current_user.is_authenticated else [])


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
            flash(f'Item {car_exists.car.name} added to cart first')
            return redirect(request.referrer)
        except Exception as e:
            print('Not updated',e)
            flash(f'Unable to add {car_exists.car.name} to cart')
            return redirect(request.referrer)
    
    new_cart_item = Cart()
    new_cart_item.quantity = 1
    new_cart_item.user_id = current_user.id
    new_cart_item.car_id = car.id 

    try:
        db.session.add(new_cart_item)
        db.session.commit()
        flash(f'Item {new_cart_item.car.name} added to cart second')
    except Exception as e:
        print(e)

    return redirect(request.referrer)
    # return render_template("add_to_cart.html", car=car)


@views.route('/cart')  # Create a route decorator for the /cart URL
@login_required
def show_cart():
    cart = Cart.query.filter_by(user_id=current_user.id).all()
    amount = 0
    for car in cart:
        amount = car.quantity * car.car.current_price
    return render_template("cart.html", cart=cart, amount=amount, total_amount=amount*1.07)


@views.route('/remove-from-cart/<int:id>')  # Create a route decorator for the /remove-from-cart/<id> URL
@login_required
def remove_from_cart(id):
    car = Cart.query.get(id)
    try:
        db.session.delete(car)
        db.session.commit()
        flash(f'Item {car.car.name} removed from cart')
    except Exception as e:
        print(e)
        flash(f'Unable to remove {car.car.name} from cart')
    return redirect(request.referrer)


@views.route('/update-cart/<int:id>', methods=['POST'])  # Create a route decorator for the /update-cart/<id> URL
@login_required
def update_cart(id):
    car = Cart.query.get(id)
    try:
        car.quantity = int(request.form.get('quantity'))
        db.session.commit()
        flash(f'Item {car.car.name} updated in cart')
    except Exception as e:
        print(e)
        flash(f'Unable to update {car.car.name} in cart')
    return redirect(request.referrer)


@views.route('/minus-from-cart/<int:id>') 
@login_required
def minus_from_cart(id):
    # Use class-bound attribute instead of a string
    car = Cart.query.options(joinedload(Cart.car)).get(id)
    
    if car is None:
        flash('Item not found in cart')
        return redirect(request.referrer)

    car_name = car.car.name  # Access car name before deletion

    try:
        if car.quantity == 1:
            db.session.delete(car)
            db.session.commit()
            flash(f'Item {car_name} removed from cart')
        else:
            car.quantity -= 1
            db.session.commit()
            flash(f'Item {car_name} quantity decreased by 1')
    except Exception as e:
        print(e)
        flash(f'Unable to decrease quantity of {car_name} in cart')
    
    return redirect(request.referrer)



@views.route('/plus-to-cart/<int:id>')  # Create a route decorator for the /plus-to-cart/<id> URL
@login_required
def plus_to_cart(id):
    car = Cart.query.get(id)

    if car is None:
        flash('Item not found in cart')
        return redirect(request.referrer)
    
    try:
        car.quantity += 1
        db.session.commit()
        flash(f'Item {car.car.name} quantity increased by 1')
    except Exception as e:
        print(e)
        flash(f'Unable to increase quantity of {car.car.name} in cart')
    return redirect(request.referrer)



