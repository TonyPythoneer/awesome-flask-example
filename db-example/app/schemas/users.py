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
emailfield = fields.Email(required=True, validate=validate.Length(max=255))
passwordfield = fields.Str(required=True, validate=validate.Length(max=64))
nicknamefield = fields.Str(validate=validate.Length(max=255))


# Request Schemas
class SignupSchema(Schema):
    email = emailfield
    password = passwordfield
    nickname = nicknamefield

    class Meta:
        strict = True


class UserDetailUpdateSchema(Schema):
    nickname = nicknamefield

    class Meta:
        strict = True


class LoginSchema(Schema):
    email = emailfield
    password = passwordfield

    class Meta:
        strict = True


class RestPasswordSchema(Schema):
    email = emailfield
    password1 = passwordfield
    password2 = fields.Str(required=True, validate=validate.Equal(comparable=password1))

    class Meta:
        strict = True
