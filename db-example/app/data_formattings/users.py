#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160129
#  @date          20160129
#  @version       0.0
"""The data formatting is designed for Users API
"""
from flask_restful import reqparse


# signup_parser
signup_parser = reqparse.RequestParser()
signup_parser.add_argument('email', type=str, required=True, location='json')
signup_parser.add_argument('password', type=str, required=True, location='json')
signup_parser.add_argument('nickname', type=str, location='json')
