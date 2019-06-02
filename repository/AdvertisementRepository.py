from contextlib import closing

import pymysql as pymysql
from flask_mysqldb import MySQL


# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'licenta'
#
# mysql = MySQL(app)

class AdvertisementRepository:

    def __init__(self, app):
        self.app = app
        self.app.config['MYSQL_HOST'] = 'localhost'
        self.app.config['MYSQL_USER'] = 'root'
        self.app.config['MYSQL_PASSWORD'] = ''
        self.app.config['MYSQL_DB'] = 'licenta'

        self.mysql = MySQL(self.app)

    def getAdvertisementPricesForDateBetween(self, date_from, date_until):
        cur = self.mysql.connection.cursor()
        query = "SELECT price, area FROM advertisement ad INNER JOIN advertisement_description des ON ad.id = des.advertisement_id WHERE (date BETWEEN '" + str(date_from) + "' AND '" + str(date_until) + "')"
        # cur.execute("SELECT price FROM advertisement WHERE (date BETWEEN '2019-05-26' AND '2019.06.02')")
        cur.execute(query)
        prices = list(cur.fetchall())
        cur.close()
        del cur

        return prices

    def getAdvertisementPricesForDateBetweenAndPreferences(self, date_from, date_until, nr_room, construction_year, distributor):
        cur = self.mysql.connection.cursor()
        query = "SELECT price, area FROM advertisement ad INNER JOIN advertisement_description des ON ad.id = des.advertisement_id" \
                                            " WHERE number_of_rooms = " + nr_room + \
                                            " AND construction_year = '" + construction_year + "'" + \
                                            " AND distributor = '" + distributor + "'" + \
                                            " AND (date BETWEEN '" + str(date_from) + "' AND '" + str(date_until) + "')"
        cur.execute(query)
        prices = list(cur.fetchall())
        cur.close()
        del cur

        return prices
