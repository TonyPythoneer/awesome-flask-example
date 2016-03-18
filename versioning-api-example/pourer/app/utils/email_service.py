#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160316
#  @date          20160316
#  @version       0.0
"""email service
"""
# level1: native python packages
from threading import Thread

# level2: native web framework packages
from flask import current_app, render_template

# level3: relative web framework plugins
from flask.ext.mail import Message

# level4: third-party packages
# None

# level5: specify-project packages
from .. import mail


def send_async_email(app, msg):
    """send_async_email"""
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, tmpl_kwargs):
    """send_email"""
    app = current_app._get_current_object()
    msg = Message(
        subject=subject,
        recipients=[to],
        html=render_template(template, **tmpl_kwargs),
    )
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr


class UserEmailService(object):
    '''UserEmailService'''

    def __init__(self, receiver):
        self.receiver = receiver

    def get_sending_mail_args(self):
        '''get_sending_mail_args'''
        return {'to': self.receiver,
                'tmpl_kwargs': {'receiver': self.receiver}}

    def send_welcome_mail(self):
        '''send_welcome_mail'''
        data = self.get_sending_mail_args()
        data['subject'] = 'Welcome pourer!'
        data['template'] = 'email_service/welcome.html'
        send_email(**data)

    def send_active_mail(self):
        '''send_active_mail'''
        data = self.get_sending_mail_args()
        data['subject'] = 'Welcome pourer!'
        data['template'] = 'email_service/welcome.html'
        send_email(**data)

    def send_forget_password_mail(self):
        '''send_forget_password_mail'''
        data = self.get_sending_mail_args()
        data['subject'] = 'Welcome pourer!'
        data['template'] = 'email_service/welcome.html'
        send_email(**data)
