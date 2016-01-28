"""

Security Helpers about werkzeug with generate_password_hash and check_password_hash:
    http://werkzeug.pocoo.org/docs/0.11/utils/#module-werkzeug.security
"""
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from .. import db
from . import mixins


class User(db.Model, mixins.CRUDMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)

    # profile fields
    email = db.Column(db.String(255), unique=True, index=True)
    password = db.Column(db.String(128))
    nickname = db.Column(db.String(255))

    # timestamp fields
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, email, password, nickname=None):
        self.account = email
        self.password = generate_password_hash(password)
        self.nickname = email or nickname

    def __repr__(self):
        return "<User(account='%s')>" % (self.account)

    def set_password(self, password):
        """The default method is sha1 to hash password"""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Verify password"""
        return check_password_hash(self.password, password)
