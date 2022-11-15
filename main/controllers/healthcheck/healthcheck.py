#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from ..base_controller import Auth, Base
from flask_restx import Namespace

api_namespace = Namespace('healthcheck', description='Estado del Servicio')

@api_namespace.route('/checkapp')
class HealthCheck(Auth, Base):
    @api_namespace.doc('Health Check de estado de servicio')
    @api_namespace.doc(security='apikey')
    @Auth.token_required
    def get(self):
        return {'status':'Alive!'}, 200
