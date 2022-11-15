#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from ..base_controller import Auth, Base, Jwt
from flask_restx import Namespace
from flask import current_app as app, request
import jwt

api_namespace = Namespace('healthcheck', description='Estado del Token JWT')

@api_namespace.route('/checkjwt')
class JWTCheck(Auth, Base, Jwt):
    @api_namespace.doc('Health Check de estado de token JWT')
    @api_namespace.doc(security='apikey')
    @Auth.token_required
    def post(self, *args, **kwargs):
        token = None
        auth_header = None

        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']

        if not auth_header:
            return {
                'status': 'NOK',
                'message': 'Authorization JWToken is missing.'
            }, 403

        token = auth_header.split(' ')[1]

        if not token:
            return {
                'status': 'NOK',
                'message': 'JWToken is missing or invalid.'
            }, 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return {
                'status': 'NOK',
                'message': 'Your JWToken is not valid. Log in for request a JWToken.'
            }, 403

        return {
            'status':'OK',
            'message': 'Your JWToken is still valid.'
        }, 200
