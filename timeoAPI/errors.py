#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# errors.py
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

from bottle import error

from timeoAPI.utils import jsondump

@error(404)
def error404(error):
    return jsondump({
        'type': 'endpoint not found',
        'status': '404'
    })

@error(500)
def error500(error):
    return jsondump({
        'type': 'server error',
        'status': '500'
    })

