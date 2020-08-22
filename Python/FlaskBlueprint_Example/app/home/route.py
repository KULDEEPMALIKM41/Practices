from app.home import home_route
from flask import render_template
@home_route.route('/')
def homepage():
    return render_template('index.html')