#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from flask import request
from flask_restx import  Namespace, fields
import json
from ..base_controller import Auth, Base, Jwt, Services

api_namespace = Namespace('apidatosgob', description='Consumo de API Rest de Datos Gob')

@api_namespace.route('/ApiDatosGob')
class ApiDatosGob(Auth, Base, Jwt, Services):
    @api_namespace.doc('Consumo de API Rest de Datos Gob')
    @api_namespace.doc(security='apikey')
    #@Auth.token_required
    #@Jwt.token_required
    def post(self, *args, **kwargs):
        payload = json.loads( request.get_data().decode("utf-8") )
        data = Services().ApiDGService().request_data(payload=payload)
        return data
