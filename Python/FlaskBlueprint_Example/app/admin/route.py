from app.admin import admin_route
from flask import render_template
@admin_route.route('/admin')
def homepage():
    return render_template('admin/index.html')