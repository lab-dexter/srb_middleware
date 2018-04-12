# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Data(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, data: float=None, time: datetime=None):  # noqa: E501
        """Data - a model defined in Swagger

        :param id: The id of this Data.  # noqa: E501
        :type id: int
        :param data: The data of this Data.  # noqa: E501
        :type data: float
        :param time: The time of this Data.  # noqa: E501
        :type time: datetime
        """
        self.swagger_types = {
            'id': int,
            'data': float,
            'time': datetime
        }

        self.attribute_map = {
            'id': 'id',
            'data': 'data',
            'time': 'time'
        }

        self._id = id
        self._data = data
        self._time = time

    @classmethod
    def from_dict(cls, dikt) -> 'Data':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Data of this Data.  # noqa: E501
        :rtype: Data
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Data.


        :return: The id of this Data.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Data.


        :param id: The id of this Data.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def data(self) -> float:
        """Gets the data of this Data.


        :return: The data of this Data.
        :rtype: float
        """
        return self._data

    @data.setter
    def data(self, data: float):
        """Sets the data of this Data.


        :param data: The data of this Data.
        :type data: float
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def time(self) -> datetime:
        """Gets the time of this Data.


        :return: The time of this Data.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time: datetime):
        """Sets the time of this Data.


        :param time: The time of this Data.
        :type time: datetime
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time
