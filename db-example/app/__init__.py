from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy

from .views import users
import configs


db = SQLAlchemy()


EXTENSIONS = (
    db,
)


BLUEPRINTS = (
    dict(blueprint=users.users_bp, url_prefix='/users'),
)



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configs.CONFIGS[config_name])

    # Initialize process: init  each ext
    for extension in EXTENSIONS:
        extension.init_app(app)

    # Initialize process: init each blueprint

    for blueprint in BLUEPRINTS:
        app.register_blueprint(**blueprint)

    return app
