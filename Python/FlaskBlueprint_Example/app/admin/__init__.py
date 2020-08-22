from flask import Blueprint
admin_route = Blueprint("admin",__name__,url_prefix='/admin_dashboard',template_folder='templates')