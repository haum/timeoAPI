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


@app.route('/v1/stations/<int:code>/<lignesens>', methods=['GET'])
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


@app.route('/v1/stations/<int:code>/coords', methods=['GET'])
def station_coords(code):
    result = meta.coords(code)
    result['type'] = "station_coords"
    return jsondump(result)


@app.route('/v1/stations/<int:code>/properties', methods=['GET'])
def station_properties(code):
    result = meta.properties(code)
    result['type'] = "station_properties"
    return jsondump(result)


@app.route('/v1/stations/<int:code>/all', methods=['GET'])
def station_allmeta(code):
    result = meta.properties(code)
    for k,v in meta.coords(code).items(): result[k] = v
    result['type'] = 'station_metadata'
    return jsondump(result)

@app.route('/v1/lines', methods=['GET'])
def lines_all():
    t = Timeo()
    result = {}
    result['type'] = 'lines'
    result['lines'] = t.get_lignes()
    return jsondump(result)


@app.route('/v1/lines/<lignesens>', methods=['GET'])
def lines_stations(lignesens):
    t = Timeo()
    result = {}
    result['type'] = 'line_stations'
    result['stations'] = t.getall_arrets(lignesens)
    return jsondump(result)
