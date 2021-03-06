import connexion
import six
import os
import MySQLdb
import logging

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

        user = os.environ["MYSQL_USER"]
        passwd = os.environ["MYSQL_PASSWORD"]
        dbhost = os.environ["MYSQL_SERVICE_HOST"]
        dbname = os.environ["MYSQL_DATABASE"]

        # TODO: Refactor DB object initialization elsewhere, e.g. during app start
        db = MySQLdb.connect(host=dbhost,
                            user=user,
                            passwd=passwd,
                            db=dbname)        

        cur = db.cursor()

        mac_id = "{}_{}".format(body.mac, body.id)
        print("Data to be inserted: {}; {}; {}".format(mac_id, body.data, body.time))
        try:
            cur.execute("""INSERT INTO `sensor_data` (`macid`, `distance`, `timestamp`) VALUES (%s, %s, %s)""",(mac_id, body.data, body.time))
            db.commit()
        except Exception as e:
            print("Failed to insert data: {}. Rollbacking db commit...".format(e))
            db.rollback()
            
        return body