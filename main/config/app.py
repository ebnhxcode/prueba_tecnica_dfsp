#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from os import environ as env

AUTH_USERNAME = env.get('AUTH_USERNAME')
AUTH_PASSWORD = env.get('AUTH_PASSWORD')

APP_NAME = env.get('APP_NAME')
APP_TITLE = env.get('APP_TITLE')
APP_DESCRIPTION = env.get('APP_DESCRIPTION')
APP_VERSION = env.get('APP_VERSION')
APP_URL_PREFIX = env.get('APP_URL_PREFIX')
APP_URL = env.get('APP_URL')
APP_HOST = env.get('APP_HOST')
APP_PORT = env.get('APP_PORT')
DEBUG = env.get('DEBUG')
THREADED = env.get('THREADED')
TIMEZONE = env.get('TIMEZONE')
FALLBACK_TIMEZONE = env.get('FALLBACK_TIMEZONE')
LOCALE = env.get('LOCALE')
FALLBACK_LOCALE = env.get('FALLBACK_LOCALE')
LOG_PATH = env.get('LOG_PATH')
PYTHONDONTWRITEBYTECODE = env.get('PYTHONDONTWRITEBYTECODE')
PYTHONUNBUFFERED = env.get('PYTHONUNBUFFERED')
PYTHONWARNINGS = env.get('PYTHONWARNINGS')

FLASK_APP = env.get('FLASK_APP')
FLASK_SECRET_KEY = env.get('FLASK_SECRET_KEY')
SECRET_KEY = env.get('SECRET_KEY')
FLASK_DEBUG = env.get('FLASK_DEBUG')
FLASK_ENV = env.get('FLASK_ENV')
ENV_FLASK = env.get('ENV_FLASK')

API_ENDPOINT = env.get('API_ENDPOINT')
API_ENDPOINT_QUERY = env.get('API_ENDPOINT_QUERY')

VALIDTOKENS = env.get('VALIDTOKENS')
X_API_KEY = env.get('X_API_KEY')
AUTHORIZATIONS = {
    'apikey' : {
        'in' : 'header',
        'type' : 'apiKey',
        'name' : 'X-API-KEY'
    }
}
