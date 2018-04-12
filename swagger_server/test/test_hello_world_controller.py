# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestHelloWorldController(BaseTestCase):
    """HelloWorldController integration test stubs"""

    def test_get_hello_world(self):
        """Test case for get_hello_world

        Get hello world response
        """
        response = self.client.open(
            '/v1/helloWorld',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
