# encoding: utf-8
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Author: Kyle Lahnakoski (kyle@lahnakoski.com)
#
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import sys

import flask
from flask import Flask
from werkzeug.wrappers import Response

from analysis import noop
from pyLibrary import convert
from pyLibrary.debugs import constants, startup
from pyLibrary.debugs.logs import Log, Except


ERROR_PAGE = """
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>Change Detector</title>
</head>
<body>
    <div style="text-align: center;position: relative;">
    <h1>Fail!</h1>
    </div>
</body>
</html>
"""

app = Flask(__name__)
config = None



@app.route('/solve', methods=['POST'])
def solve():
    try:
        response_data = convert.unicode2utf8(convert.value2json(noop.solve(flask.request.json)))

        return Response(
            response_data,
            direct_passthrough=True,  # FOR STREAMING
            status=200,
            headers={
                "access-control-allow-origin": "*",
                "content-type": "application/json"
            }
        )
    except Exception, e:
        e = Except.wrap(e)
        Log.warning("Could not proces", cause=e)
        e = e.as_dict()
        return Response(
            convert.unicode2utf8(convert.value2json(e)),
            status=400,
            headers={
                "access-control-allow-origin": "*",
                "content-type": "application/json"
            }
        )


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def default_page(path):
    return Response(
        convert.unicode2utf8(ERROR_PAGE),
        status=400,
        headers={
            "access-control-allow-origin": "*",
            "content-type": "text/html"
        }
    )


if __name__ == "__main__":
    try:
        config = startup.read_settings()
        constants.set(config.constants)
        Log.start(config.debug)

        app.run(**config.flask)
    except Exception, e:
        Log.error("Serious problem with ActiveData service!  Shutdown completed!", cause=e)
    finally:
        Log.stop()

    sys.exit(0)


