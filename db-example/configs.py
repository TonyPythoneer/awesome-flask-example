import os

import local_configs


BASEDIR = os.path.abspath(os.path.dirname(__file__))


class FlaskConfig(object):
    """It's 0.10.1 of version for flask config

    Builtin Configuration Values:
        http://flask.pocoo.org/docs/0.10/config/#builtin-configuration-values
        http://docs.jinkan.org/docs/flask/config.html#id3
    """
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'


class FlaskRestfulConfig(object):
    """It's 0.3.4 of version for flask-restful config

    ERROR_404_HELP:
        http://flask-restful-cn.readthedocs.org/en/0.3.4/quickstart.html?highlight=config#endpoints

    BUNDLE_ERRORS:
        http://flask-restful-cn.readthedocs.org/en/0.3.4/reqparse.html#error-handling
    """
    BUNDLE_ERRORS = True


class FlaskSQLAlchemyCofig(object):
    """It's 2.1 of version for Flask-SQLAlchemy config

    Configuration Keys:
        http://flask-sqlalchemy.pocoo.org/2.1/config/
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEFAULT_DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASEDIR, 'example.sqlite')
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class BaseConfig(local_configs.LocalConfig, FlaskConfig,
                 FlaskRestfulConfig, FlaskSQLAlchemyCofig):
    pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True


CONFIGS = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
}
