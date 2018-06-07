import connexion
import six
import os
import MySQLdb
import logging

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
        body = RAData.from_dict(connexion.request.get_json())  # noqa: E501

        user = os.environ["MYSQL_USER"]
        passwd = os.environ["MYSQL_PASSWORD"]
        dbhost = os.environ["MYSQL_SERVICE_HOST"]
        dbname = os.environ["MYSQL_RA_DATABASE"]

        # TODO: Refactor DB object initialization elsewhere, e.g. during app start
        db = MySQLdb.connect(host=dbhost,
                            user=user,
                            passwd=passwd,
                            db=dbname)        

        cur = db.cursor()

        # mac_id = "{}_{}".format(body.mac, body.id)
        print("Data to be inserted: {}; {}; {}".format(body.mac, body.data, body.time))
        try:
            cur.execute("""INSERT INTO `sensor_data` (`mac`, `data`, `timestamp`) VALUES (%s, %s, %s)""",(body.mac, body.data, body.time))
            db.commit()
        except Exception as e:
            print("Failed to insert data: {}. Rollbacking db commit...".format(e))
            db.rollback()
            
        return body