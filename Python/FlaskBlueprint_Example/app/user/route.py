from app.user import user_route
from flask import render_template
@user_route.route('/kuldeep')
def homepage():
    return render_template('user/index.html')