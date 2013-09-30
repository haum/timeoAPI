#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# views.py
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

from pytimeo import Timeo

from timeoAPI import app
from timeoAPI.utils import jsondump
import timeoAPI.sources.meta as meta


@app.route('/stations/<int:code>/<lignesens>', methods=['GET'])
def station_next(code, lignesens):
    t = Timeo()
    times = t.get_arret(lignesens, code)

    line,direction = lignesens.split('_')
    return jsondump({
        "type": "next_stops",
        "station": code,
        "line": line,
        "direction": direction,
        "stops": times
    })


@app.route('/stations/<int:code>/meta/coords', methods=['GET'])
def station_coords(code):
    result = meta.coords(code)
    result['type'] = "station_coords"
    return jsondump(result)


@app.route('/stations/<int:code>/meta/properties', methods=['GET'])
def station_properties(code):
    result = meta.properties(code)
    result['type'] = "station_properties"
    return jsondump(result)


@app.route('/stations/<int:code>/meta/all', methods=['GET'])
def station_allmeta(code):
    result = meta.properties(code)
    for k,v in meta.coords(code).items(): result[k] = v
    result['type'] = 'station_metadata'
    return jsondump(result)

@app.route('/lines/all', methods=['GET'])
def lines_all():
    t = Timeo()
    result = t.get_lignes()
    result['type'] = 'lines'
    return jsondump(result)


@app.route('/lines/<lignesens>/stations', methods=['GET'])
def lines_stations(linecode):
    t = Timeo()
    result = t.getall_arrets(lignesens)
    result['type'] = 'line_stations'
    return jsondump(result)
