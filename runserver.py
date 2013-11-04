#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# runserver.py
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

import bottle

import timeoAPI.views
import timeoAPI.errors
from timeoAPI.middleware import StripPathMiddleware as SPM

app = bottle.default_app()
application = SPM(app)

# bottle.debug(mode=True)

bottle.run(app= application, server='cherrypy', reloader=True)



