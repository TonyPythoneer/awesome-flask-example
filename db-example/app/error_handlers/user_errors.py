#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160202
#  @date          20106202
#  @version       0.1
"""Error handling list

Error handling naming format:
    %(API_NAME)s_ERR_%(ERROR_CODE)s_%(ERROR_EVENT)s

"""
USER_ERR_1001_REGISTERED_ACC = {
    "error_code": 1001,
    "message": "The account is registered."
}

USER_ERR_1002_INEXISTENT_ACC = {
    "code": 1002,
    "message": "Account doesn't exist"
}
