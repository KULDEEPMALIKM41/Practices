from flask import Flask, url_for
from importlib import import_module


def register_blueprints(app):
    module = import_module('app.{}.route'.format('home'))
    app.register_blueprint(module.home_route)
    module = import_module('app.{}.route'.format('user'))
    app.register_blueprint(module.user_route)
    module = import_module('app.{}.route'.format('admin'))
    app.register_blueprint(module.admin_route)

def create_app():
    app = Flask(__name__, static_folder='base/static')
    register_blueprints(app)
    return app