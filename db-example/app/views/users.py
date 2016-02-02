#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160129
#  @date          20160129
#  @version       0.0
"""Users API
"""
from flask import Blueprint, Response
from flask.views import MethodView

from webargs.flaskparser import use_args
from sqlalchemy.exc import IntegrityError

from .. import db
from ..models.users import User
from ..schemas.users import SignupSchema
from ..error_handlers import user_errors


users_bp = Blueprint('users', __name__)


class Signup(MethodView):

    @use_args(SignupSchema, locations=('json',))
    def post(self, args):
        user = User(**args)
        try:
            user.add()
        except IntegrityError as err:
            err.data = user_errors.USER_ERR_1001_REGISTERED_ACC
        return Response(status=201, mimetype="application/json")


# Url patterns: To register views in blueprint
users_bp.add_url_rule('/signup', view_func=Signup.as_view('signup'))
