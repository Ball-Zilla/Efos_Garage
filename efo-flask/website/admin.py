from flask import Blueprint, render_template, flash, request, send_from_directory, redirect
from flask_login import login_required, current_user
from .forms import add_car_form
from werkzeug.utils import secure_filename
from .models import Cars
from . import db

admin = Blueprint('admin', __name__)


@admin.route('/media/<path:filename>')
def get_media(filename):
    return send_from_directory('../media', filename)

@admin.route('/add-car', methods=['GET', 'POST'])
@login_required
def add_car():
    if current_user.id == 1:
        form = add_car_form()
        if request.method == 'POST' and form.validate_on_submit():
            # make = form.make.data
            # model = form.model.data
            year = form.year.data
            current_price = form.current_price.data
            previous_price = form.previous_price.data
            in_stock = form.in_stock.data
            discount_sale = form.discount_sale.data
            name = form.name.data
            exterior_color = form.exterior_color.data
            interior_color = form.interior_color.data
            engine = form.engine.data
            transmission = form.transmission.data
            fuel_type = form.fuel_type.data
            vin_number = form.vin_number.data
            mileage = form.mileage.data

            file = form.product_image.data

            file_name = secure_filename(file.filename)

            file_path = f'./media/{file_name}'

            file.save(file_path)

            new_car = Cars()
            # new_car.make = make
            # new_car.model = model
            new_car.year = year
            new_car.current_price = current_price
            new_car.previous_price = previous_price
            new_car.in_stock = in_stock
            new_car.discount_sale = discount_sale
            new_car.name = name
            new_car.exterior_color = exterior_color
            new_car.interior_color = interior_color
            new_car.engine = engine
            new_car.transmission = transmission
            new_car.fuel_type = fuel_type
            new_car.vin_number = vin_number
            new_car.mileage = mileage

            new_car.product_image = file_path


            try:
                db.session.add(new_car)
                db.session.commit()
                print('Car added successfully')
                flash(f'Car {name} added successfully')
                return render_template("add_car.html", form=form)
            except Exception as e:
                print(e)
                flash('Car not added!!')
                db.session.rollback()
                return render_template("add_car.html", form=form)
            
        print(form.errors)
        print('Form not validated')
        return render_template("add_car.html", form=form)
        

    return render_template("404.html")


@admin.route('/view-cars', methods=['GET', 'POST'])
@login_required
def view_cars():
    if current_user.id == 1:
        cars = Cars.query.order_by(Cars.date_created.desc()).all()
        return render_template("view_cars.html", cars=cars)
    return render_template("404.html")



@admin.route('/delete-car/<int:id>', methods=['POST'])
@login_required
def delete_car(id):
    if current_user.id == 1:
        try:
            car_del = Cars.query.get(id)
            if not car_del:
                flash('Car not found')
                return redirect('/view-cars')
            
            db.session.delete(car_del)
            db.session.commit()
            flash('Car deleted successfully')
            return redirect('/view-cars')  # Redirect instead of rendering directly
        except Exception as e:
            print(e)
            flash('Car not deleted')
            db.session.rollback()
            return redirect('/view-cars')
    return render_template("404.html")


@admin.route('/edit-car/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_car(id):
    if current_user.id == 1:
        car = Cars.query.get(id)
        form = add_car_form(obj=car)  # Automatically populate the form with car data

        if request.method == 'POST' and form.validate_on_submit():
            # Get form data
            name = form.name.data
            exterior_color = form.exterior_color.data
            interior_color = form.interior_color.data
            engine = form.engine.data
            transmission = form.transmission.data
            fuel_type = form.fuel_type.data
            vin_number = form.vin_number.data
            mileage = form.mileage.data
            year = form.year.data
            current_price = form.current_price.data
            previous_price = form.previous_price.data
            in_stock = form.in_stock.data
            discount_sale = form.discount_sale.data

            # Handle file upload
            file = form.product_image.data
            if file:
                file_name = secure_filename(file.filename)
                file_path = f'./media/{file_name}'
                file.save(file_path)
            else:
                file_path = car.product_image  # Retain the old image if no new image is uploaded

            # Update the car object
            car.name = name
            car.exterior_color = exterior_color
            car.interior_color = interior_color
            car.engine = engine
            car.transmission = transmission
            car.fuel_type = fuel_type
            car.vin_number = vin_number
            car.mileage = mileage
            car.year = year
            car.current_price = current_price
            car.previous_price = previous_price
            car.in_stock = in_stock
            car.discount_sale = discount_sale
            car.product_image = file_path  # Only change if a new file was uploaded

            # Commit changes to the database
            try:
                db.session.commit()
                flash(f'{name} updated successfully')
                print('Car updated')
                return redirect('/view-cars')
            except Exception as e:
                print(e)
                flash('Car not updated')
                db.session.rollback()

        return render_template("edit_car.html", form=form, car=car)
    
    return render_template("404.html")
