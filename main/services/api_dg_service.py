#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from flask import copy_current_request_context, current_app as app
from threading import Thread
import xmltodict, datetime, string, base64, requests, json

class ApiDGService():

    def __init__(self):
        pass

    def request_data(self, payload):
        endpoint = app.config['API_ENDPOINT_QUERY']
        offset = payload['offset']

        linea = ''
        comuna = ''

        if 'linea' in payload:
          linea = payload['linea']

        if 'comuna' in payload:
          comuna = payload['comuna']

        #print(offset)
        if offset == '0':
          query = f'&limit=50'
        else:
          query = f'&offset={offset}&limit={offset}'

        if linea != '' and comuna != '':
          query += f'&q={linea} {comuna}'
        else:
          if linea != '':
            query += f'&q={linea}'
          if comuna != '':
            query += f'&q={comuna}'



        url = f'{endpoint}{query}'
        headers = {
            'user-agent': 'api-datos-dgd/0.0.1',
            'Content-Type': "application/json"
        }
        # Override payload for sanitize, maybe can apply rut validator (*)
        try:
            response = requests.post(url=url, headers=headers)
            json_response = response.json()
            #print(json_response)
            return json_response

        except:
            return {}
            pass


        # pass
        # endpoint = app.config['API_ENDPOINT_QUERY']
        # start = '&start=50'
        # limit = '&limit=50'
        # next = '&offset=50&limit=50'
        # #query = f'{start}{next}{limit}'
        # query = '&offset=50'
        # url = f'{endpoint}{query}'
        # fileobj = urllib.request.urlopen(url)
        # data = fileobj.read()
        # return data
        # pass
