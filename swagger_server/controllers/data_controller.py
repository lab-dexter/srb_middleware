import connexion
import six
import os
import MySQLdb
import logging

from swagger_server.models.data import Data  # noqa: E501
from swagger_server import util

logger = logging.basicConfig(level=logging.DEBUG)

def add_data(body=None):  # noqa: E501
    """Add data sample

    Add data sample # noqa: E501

    :param body: Add data sample
    :type body: dict | bytes

    :rtype: Data
    """
    if connexion.request.is_json:
        body = Data.from_dict(connexion.request.get_json())  # noqa: E501

        user = os.environ["MYSQL_USER"]
        passwd = os.environ["MYSQL_PASSWORD"]
        dbhost = os.environ["MYSQL_SERVICE_HOST"]
        dbname = os.environ["MYSQL_DATABASE"]

        db = MySQLdb.connect(host=dbhost,
                            user=user,
                            passwd=passwd,
                            db=dbname)

        cur = db.cursor()
        cur.execute("SELECT * FROM `sensor_data`")
        for row in cur.fetchall():
            logger.debug("{} {} {}".format(row[0], row[1], row[2]))
            print("{} {} {}".format(row[0], row[1], row[2]))

        return body