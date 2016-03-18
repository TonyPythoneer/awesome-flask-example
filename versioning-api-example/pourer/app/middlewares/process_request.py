#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160316
#  @date          20160316
#  @version       0.0
"""process request middleware
"""
from flask import request, redirect, url_for, abort

from .. import app


@app.before_request
def versioning_api_middleware():
    # data process: necessary variables
    version = request.headers.get('HTTP_X_API_VERSION', '')
    path_list = request.path.split('/')[1:]

    # request process: stop visiting when request is invalid
    if version and path_list[0] == 'api':
        if path_list[1] != version:
            abort(403)
