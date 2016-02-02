#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160129
#  @date          20160129
#  @version       0.0
"""Users API
"""
from flask import Blueprint, Response, json
from flask.views import MethodView

from webargs.flaskparser import use_args
from sqlalchemy.exc import IntegrityError

from .. import db
from ..error_handlers import user_errors
from ..models.users import User
from ..schemas.users import SignupSchema, UserDetailUpdateSchema
from ..serializers.users import UserSerializer
from .mixins import RestfulViewMixin


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


class UserDetail(RestfulViewMixin, MethodView):
    model = User
    serializer_class = UserSerializer

    def get(self, id):
        user = self.get_object(id)
        serializer = self.get_serializer()
        data = serializer.dump(user).data
        return Response(response=json.dumps({"data": data}), status=200,
                        mimetype="application/json")

    @use_args(UserDetailUpdateSchema, locations=('json',))
    def put(self, args, id):
        user = self.get_object(id)
        user.nickname = args.get('nickname', user.nickname)
        user.update()
        return Response(status=200, mimetype="application/json")

    def delete(self, id):
        user = self.get_object(id)
        user.delete()
        return Response(status=204, mimetype="application/json")


# Url patterns: To register views in blueprint
users_bp.add_url_rule('/signup', view_func=Signup.as_view('signup'))
users_bp.add_url_rule('/<int:id>', view_func=UserDetail.as_view('user-detail'))
