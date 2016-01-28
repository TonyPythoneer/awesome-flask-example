from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy


import configs


db = SQLAlchemy()


def init_ext(app):
    EXTENSIONS = (
        db,
    )
    for extension in EXTENSIONS:
        extension.init_app(app)


def init_bp(app):
    from .views import users

    BLUEPRINTS = (
        dict(blueprint=users.users_bp, url_prefix='/users'),
    )
    for blueprint in BLUEPRINTS:
        app.register_blueprint(**blueprint)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configs.CONFIGS[config_name])

    # Initialize process: init  each ext
    init_ext(app)
    '''
    for extension in EXTENSIONS:
        extension.init_app(app)
    '''
    # Initialize process: init each blueprint
    init_bp(app)
    '''
    for blueprint in BLUEPRINTS:
        app.register_blueprint(**blueprint)
    '''
    return app
