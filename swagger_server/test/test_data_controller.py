# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.data import Data  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDataController(BaseTestCase):
    """DataController integration test stubs"""

    def test_add_data(self):
        """Test case for add_data

        Add data sample
        """
        body = Data()
        response = self.client.open(
            '/v1/data',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
