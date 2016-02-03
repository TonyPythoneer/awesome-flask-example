#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160129
#  @date          20160129
#  @version       0.0
"""The model is designed for Users API

Security Helpers about werkzeug with generate_password_hash and check_password_hash:
    http://werkzeug.pocoo.org/docs/0.11/utils/#module-werkzeug.security
"""
from datetime import datetime

from flask.ext.login import UserMixin

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


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
