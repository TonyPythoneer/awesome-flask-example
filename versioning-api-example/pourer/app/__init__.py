#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160311
#  @date          20160311
#  @version       0.0
"""Init flask app
"""
# level1: native python packages
# None

# level2: native web framework packages
from flask import Flask

# level3: relative web framework plugins
from flask.ext.mongoengine import MongoEngine
from flask.ext.mail import Mail
from flask_debugtoolbar import DebugToolbarExtension
from flask_debug_api import DebugAPIExtension

# level4: third-party packages
# None

# level5: specify-project packages
# None


# Extensions process: init extensions
app = Flask(__name__)
mail = Mail()
mongo = MongoEngine()
debug_toolbar = DebugToolbarExtension()
debug_api = DebugAPIExtension()


def versioning_api_url(blueprints, version):
    # data process: Decide url structure of the application
    prefix = '/api/%s' % version

    # data process: set the new url_prefix (create new object and avoid mutable dict)
    bps = []
    for blueprint in blueprints:
        bps.append({
            'blueprint': blueprint['blueprint'],
            'url_prefix': prefix + blueprint['url_prefix']
        })
    return bps


class FlaskApplicationFactory(object):
    '''FlaskApplicationFactory'''

    def install_middlewares(self):
        '''install_middlewares'''
        from .middlewares import process_request

    def install_extensions(self):
        '''install_extensions'''
        extensions = (
            mail,
            mongo,
            debug_toolbar,
            debug_api,
        )

        # extension porcess: app register blueprint
        for ext in extensions:
            ext.init_app(app)

    def install_blueprints(self):
        '''install_blueprint'''
        # blueprint porcess: import patterns it's ready to be registered
        from .v1.blueprints import BLUEPRINT_PATTERNS as v1_bp_patterns

        # blueprint porcess: Add version for each patterns
        blueprint_sets = (
            versioning_api_url(v1_bp_patterns, version='v1'),
        )

        # blueprint porcess: app register blueprint
        for blueprint_patterns in blueprint_sets:
            for blueprint in blueprint_patterns:
                app.register_blueprint(**blueprint)

    def install_handlers(self):
        '''install_handlers'''
        from .handlers import (
            status_code_handlers,
            mongoengine_handlers
        )

    def create_app(self, config_filename):
        '''create_app'''
        app.config.from_object(config_filename)
        self.install_middlewares()
        self.install_extensions()
        self.install_blueprints()
        self.install_handlers()
        return app
