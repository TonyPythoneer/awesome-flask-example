"""Users API
"""
from flask import Blueprint
from flask_restful import Api, Resource


users_bp = Blueprint('users', __name__)
api = Api(users_bp)


@api.resource('/foo')
class Foo(Resource):
    def get(self):
        return 'Hello, World!'
