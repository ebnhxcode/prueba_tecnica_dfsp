#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# Login
from controllers.auth.login import api_namespace as api_login
# Health Check
from controllers.healthcheck.healthcheck import api_namespace as api_hc
from controllers.healthcheck.jwtcheck import api_namespace as api_jwtc
# API Datos Gob
from controllers.apidatosgob.api_datos_gob import api_namespace as api_dg

# Add all namespaces from controllers or blueprints
API_ROUTES = {
    # Health Check
    'login': { 'route': api_login },
    # Health Check
    'healthcheck': { 'route': api_hc },
    'jwtcheck': { 'route': api_jwtc },
    # SRCeI
    'api_datos_gob': { 'route': api_dg },

}
