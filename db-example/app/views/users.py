#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160129
#  @date          20160129
#  @version       0.0
"""Users API
"""
from flask import Blueprint
from flask_restful import Api, Resource

from .. import db


users_bp = Blueprint('users', __name__)
api = Api(users_bp)


@api.resource('/foo')
class Foo(Resource):
    def get(self):
        return 'Hello, World!'
