#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# meta.py
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
Metadata for stations
"""

import os
import sqlite3
import json
import requests

from timeoAPI.utils import connect_db

def coords(code):
    """
    Get coordinates for station

    code -- station code
    """

    columns = ['code', 'lat', 'lon']

    conn = connect_db()
    c = conn.cursor()

    if type(code)==list:
        c.execute("SELECT * FROM metadata")
        all = c.fetchall()
        res = {_[0]:[_[1],_[2]] for _ in all if _[0] in code}
    else:

        c.execute("SELECT * FROM metadata WHERE code=?", (str(code),))
        res = c.fetchone()

    if res and type(res)!=dict:
        return dict(zip(columns, list(res)))
    if not res:
        return dict()
    else:
        return res

def properties(code):
    """
    Get properties for station

    code -- station code
    """
    # TODO

    return {}


class MetaInitializer:
    """
    Initializer for the metadata DB
    """

    def __init__(self, db_file, overpass_url="http://overpass-api.de/api/interpreter"):
        """
        Constructor

        db_file -- file to write to
        overpass_url -- url to Overpass API interpreter
        """

        self.db_file = db_file
        self.overpass_url = overpass_url

    def _get_conn(self):
        """
        Return a cursor for DB
        """

        return sqlite3.connect(self.db_file)

    def _insert_to_db(self, dataset):
        """
        Perform real insert
        """

        # prepare payload
        insert_list = [(_['properties']['timeo'], _['geometry']['coordinates'][1], _['geometry']['coordinates'][0]) for
                       _ in dataset['features']]

        conn = self._get_conn()
        c = conn.cursor()
        for i in insert_list:
            try:
                c.execute("INSERT INTO metadata(`code`, `lat`,`lon`) VALUES(?, ?, ?)", i)
            except sqlite3.IntegrityError: # code already added
                pass
        conn.commit()
        conn.close()

    def from_file(self, filename):
        """
        Extract data from file (json)

        filename -- name of JSON file
        """

        if not os.path.exists(filename):
            raise IOError("File "+filename+" not found.")

        with open(filename, 'r') as f:
            geodata = json.loads(f.read())

        self._insert_to_db(geodata)

    def from_overpass(self, queryfile):
        """
        Extract data from an Overpass request
        """

        with open(queryfile, 'rb') as f:
            r = requests.post(
                self.overpass_url,
                data=f
            )

        self._insert_to_db(json.loads(r.text))


