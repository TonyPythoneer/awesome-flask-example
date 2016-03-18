#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160316
#  @date          20160316
#  @version       0.0
"""Command
"""
# level1: native python packages
# None

# level2: native web framework packages
from flask import url_for

# level3: relative web framework plugins
from flask.ext.script import Command, Shell

# level4: third-party packages
# None

# level5: specify-project packages
from .. import app
from ..models.user import User
from ..models.token import Token


def make_shell_context():
    documents = {
        "User": User,
        "Token": Token
    }
    return dict(app=app, **documents)


class ListRoutes(Command):
    def run(self):
        import urllib
        output = []
        for rule in app.url_map.iter_rules():

            options = {}
            for arg in rule.arguments:
                options[arg] = "[{0}]".format(arg)

            methods = ','.join(rule.methods)
            url = url_for(rule.endpoint, **options)
            line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
            output.append(line)

        for line in sorted(output):
            print line


FLASK_COMMANDS = {
    'shell': Shell(make_context=make_shell_context),
    'list_routes': ListRoutes(),
}
