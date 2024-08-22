from flask import Blueprint, render_template  # Import the Blueprint class and the render_template function

views = Blueprint('views', __name__)  # Create a Blueprint object called views

@views.route('/')  # Create a route decorator for the / URL
def home():
    return render_template("home.html")