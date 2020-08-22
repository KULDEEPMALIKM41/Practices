from flask import Blueprint
user_route = Blueprint("user",__name__,url_prefix='/user_dashboard',template_folder='templates')