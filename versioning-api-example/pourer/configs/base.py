#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160311
#  @date          20160311
#  @version       0.0
"""BaseConfig
"""
import os

try:
    from .local import LocalConfig
except ImportError:
    raise ImportError("LocalConfig not imported")


BASEDIR = os.path.abspath(os.path.dirname(__file__))


class FlaskConfig(object):
    """It's 0.10.1 of version for flask config

    Builtin Configuration Values:
        http://flask.pocoo.org/docs/0.10/config/#builtin-configuration-values
        http://docs.jinkan.org/docs/flask/config.html#id3
    """
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'


class FlaskDebugToolbar(object):
    """https://flask-debugtoolbar.readthedocs.org/en/latest/#configuration
    """
    #DEBUG_TB_HOSTS = 'localhost'
    DEBUG_TB_PANELS = [
        'flask_debugtoolbar.panels.versions.VersionDebugPanel',
        'flask_debugtoolbar.panels.timer.TimerDebugPanel',
        'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
        'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
        'flask_debugtoolbar.panels.template.TemplateDebugPanel',
        'flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel',
        'flask_debugtoolbar.panels.logger.LoggingPanel',
        'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
        # Add the MongoDB panel
        'flask.ext.mongoengine.panels.MongoDebugPanel',
        'flask_debug_api.BrowseAPIPanel',
    ]
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class BaseConfig(LocalConfig, FlaskConfig, FlaskDebugToolbar):
    """Input your config of installed package in inheritance objects of BaseConfig
    """
