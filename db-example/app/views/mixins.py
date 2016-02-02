#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160202
#  @date          20160202
#  @version       0.0
"""There is copied from django rest framework's generics.py

https://github.com/tomchristie/django-rest-framework/blob/master/rest_framework/generics.py
"""
from flask import abort


class RestfulViewMixin(object):
    """Simplify leveraging database"""
    model = None
    serializer_class = None

    def get_object(self, ident):
        """It's copied from Django rest framework.

        https://github.com/tomchristie/django-rest-framework/blob/master/rest_framework/generics.py#L14

        https://github.com/tomchristie/django-rest-framework/blob/master/rest_framework/generics.py#L76
        """
        if not self.model:
            abort(500)
        return self.model.query.get_or_404(ident)

    def get_serializer(self, *args, **kwargs):
        """It's copied from Django rest framework.

        https://github.com/tomchristie/django-rest-framework/blob/master/rest_framework/generics.py#L104
        """
        if not self.serializer_class:
            abort(500)
        serializer_class = self.serializer_class()
        return serializer_class

    '''
    def get_response(self):
        return Response(response=None, status=200)
    '''
