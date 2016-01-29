# encoding: utf-8
#
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

import requests

from pyLibrary import convert, jsons
from pyLibrary.testing.fuzzytestcase import FuzzyTestCase


settings = jsons.ref.get("file://tests/config/test_settings.json")


class TestRequests(FuzzyTestCase):
    """
    TEST THAT THE SERVICE RESPONDS
    """

    def test_request(self):
        # SIMPLEST POSSIBLE REQUEST (NOTHING IMPORTANT HAPPENING)
        data = {
            "meta": {
                "suite": "sessionrestore_no_auto_restore osx-10-10",
                "platform": "osx-10-10",
                "e10s": False,
                "och": "opt",
                "bucket": "startup",
                "statistic": "mean"
            },
            "header": ["rownum", "timestamp", "revision", "value"],
            "data": [
                [1, "2015-12-06 09:21:15", "18339318", 879],
                [2, "2015-12-06 16:50:36", "18340858", 976],
                [3, "2015-12-06 19:01:54", "18342319", 880],
                [4, "2015-12-06 21:08:56", "18343567", 1003],
                [5, "2015-12-06 23:33:27", "18345266", 1002],
                [6, "2015-12-07 02:16:22", "18347807", 977],
                [7, "2015-12-07 02:18:29", "18348057", 1035],
                [8, "2015-12-07 04:51:52", "18351263", 1032],
                [9, "2015-12-07 05:29:42", "18351078", 1035],
                [10, "2015-12-07 05:50:37", "18351749", 1010]
            ]
        }

        response = requests.post(settings.url, json=data)
        self.assertEqual(response.status_code, 200)
        data = convert.json2value(convert.utf82unicode(response.content))
        self.assertEqual(data, {})

    def test_bad_request(self):
        # SIMPLEST POSSIBLE REQUEST (NOTHING IMPORTANT HAPPENING)
        response = requests.post(settings.url, data=b"bad exmaple")
        self.assertEqual(response.status_code, 400)
