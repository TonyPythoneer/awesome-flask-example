#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160129
#  @date          20160129
#  @version       0.0
"""Users API
"""
from flask import Blueprint, Response, json, request
from flask.views import MethodView
from webargs.flaskparser import use_args

from .. import db
from ..models.users import User
from ..data_formattings.users import signup_parser
from ..schemas.users import SignupSchema


users_bp = Blueprint('users', __name__)


class Signup(MethodView):

    @use_args(SignupSchema, locations=('json',))
    def post(self, args):
        print args

        return 'OK', 200


users_bp.add_url_rule('/signup', view_func=Signup.as_view('signup'))
