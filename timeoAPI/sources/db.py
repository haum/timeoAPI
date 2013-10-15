#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# db.py
#
# Copyright © 2013 Mathieu Gaborit (matael) <mathieu@matael.org>
#
#
# Distributed under WTFPL terms
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.
#

"""
DB related tools (input only)
"""

import logging

import pymongo as mongo

from pytimeo import Timeo

log = logging.getLogger(__name__)

class MongoDBInitializer:

    def __init__(self, host="localhost", port=27017, dbname='timeoapi'):

        self.conn = mongo.MongoClient(host, port)
        self.db = self.conn[dbname]
        if not "stations" in self.db.collection_names():
            log.info("Collection 'stations' not found. Creating it...")
            self.db.create_collection("stations")
            self.stations = self.db['stations']
        if not "lines" in self.db.collection_names():
            log.info("Collection 'lines' not found. Creating it...")
            self.db.create_collection("lines")
            self.lines = self.db['lines']

    def geo_from_file(self, filename):
        """
        Extract data from file (json)

        filename -- name of JSON file
        """

        if not os.path.exists(filename):
            raise IOError("File "+filename+" not found.")

        with open(filename, 'r') as f:
            geodata = json.loads(f.read())

        insert_list = [
            {'code': _['properties']['timeo'],
             'coords': [_['geometry']['coordinates'][1],
                        _['geometry']['coordinates'][0]]
            } for _ in geodata['features']]

        self.stations.insert(insert_list)

    def _get_all_timeo_data(self):
        """
        This fonction will do 2 different things :
            - find the complete list for lines and store it in self.timeodata[lines]
            - find all stations and bind them to their name and the lines passing by
                (in self.timeodata[stations])
        """

        t = Timeo()
        self.timeodata = {}
        self.timeodata['lines'] = t.get_lines()
        self.timeodata['stations'] = {}

        for l in self.timeodata['lines'].values():
            arrets_ligne = t.getall_arrets(l)
            for code,name in arrets_ligne.items():
                self.stations.insert({
                    "code": code,
                    "name": name
                })


    def add_names(self):
        """
        This function should run only on full service hours.
        It Will look in every line and find all stations. Then, it will grab
        stations name and add them to the DB
        """

        pass # TODO : write this function or delete boilerplate if useless