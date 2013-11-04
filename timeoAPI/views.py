#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# views.py
#
# Copyright © 2013 Mathieu Gaborit (matael) <mathieu@matael.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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

    # TODO: A améliorer
    t = Timeo()
    result = {}
    result['type'] = 'line_stations'
    result['stations'] = t.getall_arrets(lignesens)

    coords = meta.coords(list(result['stations'].keys()))
    if not set(result['stations'].keys()) == set(coords.keys()):
        for i in set(result['stations'].keys())-set(coords.keys()):
            coords[i] = []
    for code in result['stations'].keys():
        result['stations'][code] = {
            'coords': coords[code],
            'name': result['stations'][code]
        }

    return jsondump(result)

@route('/v1/lines/<lignesens>/stops', 'GET')
def next_times(lignesens):
    t = Timeo()
    codes = t.getall_arrets(lignesens)

    times = {}
    for code in codes:
        times[code] = t.get_arret(lignesens, code)

    return jsondump({
        "type": "multiple_next_stops",
        "stops": times
    })

