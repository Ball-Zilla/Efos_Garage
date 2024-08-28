from . import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    username = db.Column(db.String(150), nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)


    cart_items = db.relationship('Cart', backref='user', lazy=True)  # cart_items = db.relationship('Cart', backref=db.backref('customer', lazy=True))
    orders = db.relationship('Orders', backref='user', lazy=True)



    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password=password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password=password)
    
    def __repr__(self):
        return f'<User {self.username, self.id, self.password}>'
    
    def __str__(self):
        return f'<User {self.id}>'
    

class Cars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # make = db.Column(db.String(50), nullable=False)
    # model = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    current_price = db.Column(db.Float, nullable=True)
    previous_price = db.Column(db.Float, nullable=True)
    in_stock = db.Column(db.Integer, default=True)
    product_image = db.Column(db.String(1500), nullable=True)
    discount_sale = db.Column(db.Boolean, default=True)
    date_created = db.Column(db.DateTime, default=datetime.now)
    exterior_color = db.Column(db.String(150), nullable=True)
    interior_color = db.Column(db.String(150), nullable=True)
    engine = db.Column(db.String(150), nullable=True)
    transmission = db.Column(db.String(150), nullable=True)
    fuel_type = db.Column(db.String(150), nullable=True)
    vin_number = db.Column(db.Integer, nullable=True)
    mileage = db.Column(db.Integer, nullable=True)
    

    cart_items = db.relationship('Cart', backref='car', lazy=True)  # cart_items = db.relationship('Cart', backref=db.backref('product', lazy=True))
    orders = db.relationship('Orders', backref='car', lazy=True)
    
    def __repr__(self):
        return f'<Car {self.make, self.model, self.year, self.current_price}>'
    
    def __str__(self):
        return f'<Car {self.id}>'
    
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=False)

    
    def __repr__(self):
        return f'<Cart {self.id, self.quantity}>'
    
    def __str__(self):
        return f'<Cart {self.id}>'
    

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(150), nullable=False)
    payment_id = db.Column(db.String(150), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable  = False)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=False)

    def __repr__(self):
        return f'<Order {self.id, self.quantity, self.total_price, self.status, self.payment_id}>'
    
    def __str__(self):
        return f'<Order {self.id}>'
    