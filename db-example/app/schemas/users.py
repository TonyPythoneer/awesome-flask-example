#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160121
#  @date          20160121
"""schemas

Field classes for various types of data.
    http://marshmallow.readthedocs.org/en/latest/api_reference.html#module-marshmallow.fields

“Read-only” and “Write-only” Fields
    https://marshmallow.readthedocs.org/en/latest/quickstart.html#read-only-and-write-only-fields

Meta
    http://marshmallow.readthedocs.org/en/latest/api_reference.html#marshmallow.Schema.Meta
"""
from marshmallow import Schema, fields, validate


class SignupSchema(Schema):
    email = fields.Email(required=True, validate=validate.Length(max=255))
    password = fields.Str(required=True, validate=validate.Length(max=64))
    nickname = fields.Str(validate=validate.Length(max=255))

    class Meta:
        strict = True


class UserDetailUpdateSchema(Schema):
    nickname = fields.Str(validate=validate.Length(max=255))

    class Meta:
        strict = True


class LoginSchema(Schema):
    email = fields.Email(required=True, validate=validate.Length(max=255))
    password = fields.Str(required=True, validate=validate.Length(max=64))

    class Meta:
        strict = True


class RestPasswordSchema(Schema):
    email = fields.Email(required=True, validate=validate.Length(max=255))
    password1 = fields.Str(required=True, validate=validate.Length(max=64))
    password2 = fields.Str(required=True, validate=validate.Equal(comparable=password1))

    class Meta:
        strict = True
