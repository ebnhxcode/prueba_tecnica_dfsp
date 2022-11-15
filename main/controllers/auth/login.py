#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from flask import current_app as app, make_response, request, session
from flask_restx import  Namespace, fields
import json, jwt, datetime
from ..base_controller import Auth, Base, Services

api_namespace = Namespace('auth', description='Request the JWT access token')

@api_namespace.route('/login')
class Login(Auth, Base):
    @api_namespace.doc('Request the JWT access token')
    @api_namespace.doc(security='apikey')
    @Auth.token_required
    @Auth.basic_required
    def post(self, *args, **kwargs):
        auth = request.authorization
        token = jwt.encode({
            'user': auth.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
        }, app.config['SECRET_KEY'])
        return {'token': token.decode('UTF-8')}
