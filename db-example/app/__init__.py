#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160129
#  @date          20160129
#  @version       0.0
"""Init flask app
"""
from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.marshmallow import Marshmallow

import configs


# Initializing process: This list is created extension object
db = SQLAlchemy()
ma = Marshmallow()


def init_exts(app):
    '''Initializing the flask app with extensions'''
    extensions = (
        db,
        ma,  # Flask-SQLAlchemy must be initialized before Flask-Marshmallow.
    )
    for extension in extensions:
        extension.init_app(app)


def init_bps(app):
    '''Initializing the flask app with blueprints'''
    from .views import users

    buleprints = (
        dict(blueprint=users.users_bp, url_prefix='/users'),
    )
    for blueprint in buleprints:
        app.register_blueprint(**blueprint)


def create_app(config_name):
    '''It's a factory.'''
    app = Flask(__name__)
    app.config.from_object(configs.CONFIGS[config_name])

    # Initializing process: Initializing the flask app with extensions
    init_exts(app)

    # Initializing process: Initializing the flask app with blueprints
    init_bps(app)

    # temp: errorhandler
    @app.errorhandler(400)
    def handle_bad_request_by_reqparse(err):
        from flask import jsonify
        res_data = {
            'message': 'Bad Request',
            'errors': err.data['message']
        }
        return jsonify(res_data), 400

    return app
