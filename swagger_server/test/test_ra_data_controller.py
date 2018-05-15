# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.ra_data import RAData  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRaDataController(BaseTestCase):
    """RaDataController integration test stubs"""

    def test_add_ra_data(self):
        """Test case for add_ra_data

        Add data sample for room availability
        """
        body = RAData()
        response = self.client.open(
            '/v1/ra_data',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
