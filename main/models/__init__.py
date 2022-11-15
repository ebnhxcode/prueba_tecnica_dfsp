#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from flask import current_app
from pymongo import MongoClient


class Model():

    _table = str
    _primary_key = str
    _driver = str
    _db = None
    _connection = None

    def __init__(self, table, primary_key, driver = None):
        self._table = table
        self._primary_key = primary_key
        self._driver = driver or current_app.config['DB_CONNECTION_DRIVER_DEFAULT']
        pass
    

    def getDatabaseConnection(self):
        if current_app.config['ACTIVE_CONNECTIONS'] != {}:
            self._connection = current_app.config['ACTIVE_CONNECTIONS'][self._driver]['connection']
            return self._connection

        connections = current_app.config['DB_CONNECTIONS']
        config = connections[self._driver]
        return self.connectDatabase(config)

    def connectDatabase(self, config):
        self._connection = None
        
        
        if config['driver'] == 'mongodb':    
            
            self._connection = MongoClient(
                f'{config["host"]}:{config["port"]}',
                username=f'{config["username"]}',
                password=f'{config["password"]}',
                authSource=f'{config["auth_source"]}',
                authMechanism=f'{config["auth_mechanism"]}'
            )

            self._connection = self._connection[config["database"]]

        elif config['driver'] == 'mysql':
            pass

        return self._connection



    @staticmethod
    def create(self):
        pass

    @staticmethod
    def save(self):
        pass

    @staticmethod
    def update(self):
        pass

    @staticmethod
    def find(self):
        pass

    @staticmethod
    def destroy(self):
        pass

    @staticmethod
    def belongsTo(self):
        pass

    @staticmethod
    def hasMany(self):
        pass

    @staticmethod
    def hasOne(self):
        pass