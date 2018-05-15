import connexion
import six

from swagger_server.models.ra_data import RAData  # noqa: E501
from swagger_server import util


def add_ra_data(body=None):  # noqa: E501
    """Add data sample for room availability

    Add data sample for room availability # noqa: E501

    :param body: Add data sample for room availability
    :type body: dict | bytes

    :rtype: RAData
    """
    if connexion.request.is_json:
        body = Data.from_dict(connexion.request.get_json())  # noqa: E501
        return body