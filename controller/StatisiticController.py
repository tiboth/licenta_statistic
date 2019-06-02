import json

from flask import request, Flask, Response
from flask_restful import Resource, Api

from service.PriceFluctuationService import PriceFluctuationService

app = Flask(__name__)
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'licenta'
# mysql = MySQL(app)

api = Api(app)


class StatisticController(Resource):

    def __init__(self, service):
        self.price_fluctuation_service = service

    # def getPriceForAdvertisement(self):
    #     cur = mysql.connection.cursor()
    #     cur.execute('''SELECT price FROM advertisement''')
    #     prices = cur.fetchall()
    #     return str(prices)

    def post(self):
        if request.headers['Content-Type'] == 'application/json':
            print("Request received")
            request_content = request.get_json()
            print('nr_rooms:: ' + request_content['nr_rooms'])
            print('old_building: ' + request_content['construction_year'])
            print('new_building: ' + request_content['distributor'])
            result = price_fluctuation_service.define_price_fluctuation(request_content['nr_rooms'],
                                                                        request_content['construction_year'],
                                                                        request_content['distributor'])
            response = Response(response=json.dumps(result.__dict__),
                                status=200,
                                mimetype="application/json")
            return response
        else:
            return "Unsupported Media Type!"


price_fluctuation_service = PriceFluctuationService(app)
api.add_resource(StatisticController, '/statistic', resource_class_kwargs={'service': price_fluctuation_service})
