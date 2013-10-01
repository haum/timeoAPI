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

from bottle import route

from pytimeo import Timeo

from timeoAPI.utils import jsondump
import timeoAPI.sources.meta as meta


@route('/v1/stations/<code:int>/coords', 'GET')
def station_coords(code):
    result  = {}
    result['type'] = "station_coords"
    result['code'] = code
    coords = meta.coords(code)
    result['coords'] = [coords['lat'], coords['lon']]
    return jsondump(result)


@route('/v1/stations/<code:int>/properties', 'GET')
def station_properties(code):
    result  = {}
    result['type'] = "station_coords"
    result['code'] = code
    result['properties'] = meta.properties(code)
    return jsondump(result)

@route('/v1/stations/<code:int>/all', 'GET')
@route('/v1/stations/<code:int>', 'GET')
def station_allmeta(code):
    result = {}
    result['type'] = 'station_metadata'
    result['code'] = code
    coords = meta.coords(code)
    result['coords'] = [coords['lat'], coords['lon']]
    result['properties'] = meta.properties(code)
    return jsondump(result)

@route('/v1/stations/<code:int>/<lignesens>', 'GET')
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

@route('/v1/lines', 'GET')
def lines_all():
    t = Timeo()
    result = {}
    result['type'] = 'lines'
    result['lines'] = t.get_lignes()
    return jsondump(result)


@route('/v1/lines/<lignesens>', 'GET')
def lines_stations(lignesens):
    t = Timeo()
    result = {}
    result['type'] = 'line_stations'
    result['stations'] = t.getall_arrets(lignesens)
    return jsondump(result)
