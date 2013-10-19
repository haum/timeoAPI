#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# utils.py
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

"""
Utilities
"""

import sqlite3
from bottle import request
from timeoAPI.settings import DATABASE_URI

def jsondump(obj):
    """
    Serialize object to compact json

    obj -- object to serialize
    """

    if (request.query.callback):
        return "%s(%s)" % (request.query.callback, obj)
    return obj


def connect_db():
    return sqlite3.connect(DATABASE_URI)


