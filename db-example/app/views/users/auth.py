#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160129
#  @date          20160129
#  @version       0.0
"""auth for Users API
"""
from flask.views import MethodView

from sqlalchemy.exc import IntegrityError
from webargs.flaskparser import use_args

from . import users_bp
from ..mixins import RestfulViewMixin
from ...models.users import User
from ...schemas.users import SignupSchema, LoginSchema
from ...error_handlers import user_errors


class SignupView(RestfulViewMixin, MethodView):

    @use_args(SignupSchema, locations=('json',))
    def post(self, args):
        user = User(**args)
        try:
            user.add()
        except IntegrityError as err:
            err.data = user_errors.USER_ERR_1001_REGISTERED_ACC
            raise
        return self.get_response(status=201)


class LoginView(RestfulViewMixin, MethodView):

    @use_args(LoginSchema, locations=('json',))
    def post(self):
        pass

class LogoutView(RestfulViewMixin, MethodView):
    pass


# Url patterns: To register views in blueprint
users_bp.add_url_rule('/signup', view_func=SignupView.as_view('signup'))
users_bp.add_url_rule('/login', view_func=LoginView.as_view('login'))
users_bp.add_url_rule('/logout', view_func=LogoutView.as_view('logout'))
