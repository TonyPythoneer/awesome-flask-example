#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160129
#  @date          20160129
#  @version       0.0
"""The model is designed for Users API

Security Helpers about werkzeug with generate_password_hash and check_password_hash:
    http://werkzeug.pocoo.org/docs/0.11/utils/#module-werkzeug.security
"""
import binascii
from datetime import datetime, timedelta
import os

from flask.ext.login import UserMixin, make_secure_token

from werkzeug.security import generate_password_hash, check_password_hash

from . import mixins
from .. import db, login_manager


class User(UserMixin, mixins.CRUDMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)

    # profile fields
    email = db.Column(db.String(255), unique=True, index=True)
    password = db.Column(db.String(128))
    nickname = db.Column(db.String(255))

    # timestamp fields
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # relationship
    devices = db.relationship('Device', backref='device', lazy='dynamic')

    last_login = db.Column(db.DateTime)
    key = relationship("Token", uselist=False, backref=db.backref("User", uselist=False))

    def __init__(self, email, password, nickname=None):
        self.email = email
        self.password = generate_password_hash(password)
        self.nickname = email or nickname

    def __repr__(self):
        return "<User(email='%s')>" % (self.email)

    def set_password(self, password):
        """The default method is sha1 to hash password"""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Verify password"""
        return check_password_hash(self.password, password)

    @classmethod
    def authenticate(cls, email=None, password=None):
        """Get the user"""
        user = cls.query.filter_by(email=email).first()
        if not user.check_password(password):
            return None
        return user

    def login(self):
        self.last_login = datetime.utcnow()
        token = Token.query.first(self)
        if token:
            return token
        token.generate_key()
        token.save()
        return token

    def logout(self):
        token = Token.query.first(self)
        if token:
            token.delete()

    def is_expired(self):
        return self.token.is_expired()


class Token(mixins.CRUDMixin, db.Model):
    __tablename__ = 'token'
    AUTH_TOKEN_DURATION = 60*60

    key = db.Column(db.String(40), unique=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="Token")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def generate_key(self):
        self.key = binascii.hexlify(os.urandom(20)).decode()
        return self.key

    def is_expired(self):
        diff = datetime.utcnow - self.created_at
        return diff > timedelta(seconds=self.AUTH_TOKEN_DURATION)


@login_manager.request_loader
def load_request(request):
    api_key = request.headers.get('Authorization', '')
    if api_key:
        user = User.query.filter_by(key=api_key).first()
        if user:
            return user
    return None


@login_manager.unauthorized_handler
def unauthorized_handler():
    from flask import jsonify
    return jsonify({"message": "Unauthorized"}), 401
