import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class LocalConfig(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'example.sqlite')
