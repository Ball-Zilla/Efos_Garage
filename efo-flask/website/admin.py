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
        items = Cars.query.order_by(Cars.date_created.desc()).all()
        return render_template("view_cars.html", items=items)
    return render_template("404.html")



@admin.route('/delete-car/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_car(id):
    if current_user.id == 1:
        car = Cars.query.get(id)
        db.session.delete(car)
        db.session.commit()
        flash('Car deleted successfully')
        return render_template("delete_car.html")
    return render_template("404.html")


@admin.route('/edit-car/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_car(id):
    if current_user.id == 1:
        car = Cars.query.get(id)
        form = add_car_form()

        form.name.data.render_kw = {'placeholder': car.name}
        form.exterior_color.data.render_kw = {'placeholder': car.exterior_color}
        form.interior_color.data.render_kw = {'placeholder': car.interior_color}
        form.engine.data.render_kw = {'placeholder': car.engine}
        form.transmission.data.render_kw = {'placeholder': car.transmission}
        form.fuel_type.data.render_kw = {'placeholder': car.fuel_type}
        form.vin_number.data.render_kw = {'placeholder': car.vin_number}
        form.mileage.data.render_kw = {'placeholder': car.mileage}
        # form.make.data.render_kw = {'placeholder': car.make}
        # form.model.data.render_kw = {'placeholder': car.model}
        form.year.data.render_kw = {'placeholder': car.year}
        form.current_price.data.render_kw = {'placeholder': car.current_price}
        form.previous_price.data.render_kw = {'placeholder': car.previous_price}
        form.in_stock.data.render_kw = {'placeholder': car.in_stock}
        form.discount_sale.data.render_kw = {'placeholder': car.discount_sale}


        if request.method == 'POST' and form.validate_on_submit():
            name = form.name.data
            exterior_color = form.exterior_color.data
            interior_color = form.interior_color.data
            engine = form.engine.data
            transmission = form.transmission.data
            fuel_type = form.fuel_type.data
            vin_number = form.vin_number.data
            mileage = form.mileage.data
            # make = form.make.data
            # model = form.model.data
            year = form.year.data
            current_price = form.current_price.data
            previous_price = form.previous_price.data
            in_stock = form.in_stock.data
            discount_sale = form.discount_sale.data

            file = form.product_image.data

            file_name = secure_filename(file.filename)
            file_path = f'./media/{file_name}'

            file.save(file_path)

            try: 
                car.query.filter_by(id=id).update(dict(name=name, exterior_color=exterior_color, 
                                                        interior_color=interior_color, engine=engine, 
                                                        transmission=transmission, fuel_type=fuel_type, 
                                                        vin_number=vin_number, mileage=mileage, year=year, 
                                                        current_price=current_price, previous_price=previous_price, 
                                                        in_stock=in_stock, discount_sale=discount_sale, 
                                                        product_image=file_path))

                db.session.commit()
                flash(f'{name} updated Successfully')
                print('Car Upadted')
                return redirect('/view-cars')
            except Exception as e:
                print(e)
                flash('Car not updated')
                db.session.rollback()
        
        return render_template("edit_car.html", form=form, car=car)
    return render_template("404.html")
