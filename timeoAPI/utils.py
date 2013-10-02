#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# utils.py
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


