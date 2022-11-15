#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, Flask
from flask_restx import Api
from flask_cors import CORS

# 0: Import de rutas y config base
from routes import API_ROUTES
from config.app import APP_TITLE, \
    APP_VERSION, \
    APP_DESCRIPTION, \
    APP_URL_PREFIX, \
    AUTHORIZATIONS

# 1: se crea aplicación y asocia config file
app = Flask(__name__, instance_relative_config=False)
# app.url_map.strict_slashes = False
app.config.from_object('config.app')
CORS(app, resources={r"/api/*": {"origins": ['http://192.168.50.16:3333', 'http://localhost:3333']}}, supports_credentials=True)


# 2: se inyectan los modulos mediante namespaces -> rutas y planos (colecciones de rutas para metodos http)
blueprint = Blueprint('api', __name__, url_prefix=APP_URL_PREFIX)

api = Api(blueprint,
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
    authorizations=AUTHORIZATIONS
)

for api_route in API_ROUTES:
    route = API_ROUTES[api_route]['route']
    api.add_namespace(route, path='')

# 3: se registran las rutas y se asocian a la aplicación
app.register_blueprint(blueprint)

# 4: se deja la responsabilidad a gunicorn de correr la app, por lo tanto no se especifica un run de __main__ basado en __name__
# app.run(debug=True)
