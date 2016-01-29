#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160129
#  @date          20160129
#  @version       0.0
"""Users API
"""
from flask import Blueprint, Response, json
from flask.views import MethodView

from .. import db
from ..models.users import User
from ..data_formattings.users import signup_parser


users_bp = Blueprint('users', __name__)


class Signup(MethodView):
    def post(self):
        args = signup_parser.parse_args()
        return 'OK', 200

'''
@users_bp.app_errorhandler(400)
def fuck(err):
    res_data = json.dumps(err.data)
    return Response(response=res_data, status=400, mimetype="application/json")
'''

users_bp.add_url_rule('/signup', view_func=Signup.as_view('signup'))
