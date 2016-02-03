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

# Field definations
class CommonFields(object):
    emailfield = fields.Email(required=True, validate=validate.Length(max=255))
    passwordfield = fields.Str(required=True, validate=validate.Length(max=64))
    nicknamefield = fields.Str(validate=validate.Length(max=255))


# Request Schemas
class SignupSchema(Schema):
    email = CommonFields.emailfield
    password = CommonFields.passwordfield
    nickname = CommonFields.nicknamefield

    class Meta:
        strict = True


class ProfileUpdateSchema(Schema):
    nickname = CommonFields.nicknamefield

    class Meta:
        strict = True


class LoginSchema(Schema):
    email = CommonFields.emailfield
    password = CommonFields.passwordfield

    class Meta:
        strict = True


class RestPasswordSchema(Schema):
    email = CommonFields.emailfield
    password1 = CommonFields.passwordfield
    password2 = fields.Str(required=True, validate=validate.Equal(comparable=password1))

    class Meta:
        strict = True
