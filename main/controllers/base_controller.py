#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from flask import copy_current_request_context, current_app as app, make_response, request
from threading import Thread
from flask_restx import Resource

from os import environ as env
from functools import wraps

import xmltodict, datetime, string, base64, requests, json, jwt

class Auth():
    @staticmethod
    def basic_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            auth = request.authorization
            # Also can attempt with database users, but for practical purposes we used static credentials
            if not auth or (auth and auth.username != app.config['AUTH_USERNAME'] and auth.password != app.config['AUTH_PASSWORD']):
                return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
            return f(*args, **kwargs)
        return decorated

    @staticmethod
    def token_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            if 'X-API-KEY' in request.headers:
                token = request.headers['X-API-KEY']
            if not token:
                return {'message': 'Token is missing.'}, 403
            # For multiple tokens or tokens to share
            if token not in app.config['VALIDTOKENS'].split(','):
                return {'message': 'Your api token is not on the list. Check your api token.'}, 403
            # For single token
            #if token != app.config['X_API_KEY']:
                #return {'message': 'Your api token is wrong. Check your api token.'}
            return f(*args, **kwargs)
        return decorated

class Jwt():
    @staticmethod
    def token_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            auth_header = None

            if 'Authorization' in request.headers:
                auth_header = request.headers['Authorization']

            if not auth_header:
                return {'message': 'Authorization JWToken is missing.'}, 403

            token = auth_header.split(' ')[1]

            if not token:
                return {'message': 'JWToken is missing or invalid.'}, 403

            try:
                data = jwt.decode(token, app.config['AUTH_PASSWORD'])
            except:
                return {'message': 'Your JWToken is not valid. Log in for request a JWToken.'}, 403

            return f(*args, **kwargs)
        return decorated


class Base(Resource):
    pass


class Services():
    from services import \
        ApiDGService

    def __init__(self):
        pass

