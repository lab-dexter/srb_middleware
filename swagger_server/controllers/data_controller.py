import connexion
import six

from swagger_server.models.data import Data  # noqa: E501
from swagger_server import util


def add_data(body=None):  # noqa: E501
    """Add data sample

    Add data sample # noqa: E501

    :param body: Add data sample
    :type body: dict | bytes

    :rtype: Data
    """
    if connexion.request.is_json:
        body = Data.from_dict(connexion.request.get_json())  # noqa: E501
        return body