# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RAData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, mac: str=None, data: float=None, time: datetime=None):  # noqa: E501
        """RAData - a model defined in Swagger

        :param mac: The mac of this RAData.  # noqa: E501
        :type mac: str
        :param data: The data of this RAData.  # noqa: E501
        :type data: float
        :param time: The time of this RAData.  # noqa: E501
        :type time: datetime
        """
        self.swagger_types = {
            'mac': str,
            'data': float,
            'time': datetime
        }

        self.attribute_map = {
            'mac': 'mac',
            'data': 'data',
            'time': 'time'
        }

        self._mac = mac
        self._data = data
        self._time = time

    @classmethod
    def from_dict(cls, dikt) -> 'RAData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RA_data of this RAData.  # noqa: E501
        :rtype: RAData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mac(self) -> str:
        """Gets the mac of this RAData.


        :return: The mac of this RAData.
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac: str):
        """Sets the mac of this RAData.


        :param mac: The mac of this RAData.
        :type mac: str
        """
        if mac is None:
            raise ValueError("Invalid value for `mac`, must not be `None`")  # noqa: E501

        self._mac = mac

    @property
    def data(self) -> float:
        """Gets the data of this RAData.


        :return: The data of this RAData.
        :rtype: float
        """
        return self._data

    @data.setter
    def data(self, data: float):
        """Sets the data of this RAData.


        :param data: The data of this RAData.
        :type data: float
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def time(self) -> datetime:
        """Gets the time of this RAData.


        :return: The time of this RAData.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time: datetime):
        """Sets the time of this RAData.


        :param time: The time of this RAData.
        :type time: datetime
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time
