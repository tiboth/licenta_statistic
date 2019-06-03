import json

from flask import request, Flask, Response
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api

from service.PriceFluctuationService import PriceFluctuationService

app = Flask(__name__)
api = Api(app)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)


class StatisticController(Resource):

    def __init__(self, service):
        self.price_fluctuation_service = service

    def post(self):
        if request.headers['Content-Type'] == 'application/json':
            print("Request received")
            request_content = request.get_json()
            print('nr rooms:: ' + request_content['nrRooms'])
            print('old building: ' + request_content['constructionYear'])
            print('new building: ' + request_content['distributor'])
            result = price_fluctuation_service.define_price_fluctuation(request_content['nrRooms'],
                                                                        request_content['constructionYear'],
                                                                        request_content['distributor'])
            response = Response(response=json.dumps(result.__dict__),
                                status=200,
                                mimetype="application/json")

            return response
        else:
            return "Unsupported Media Type!"


price_fluctuation_service = PriceFluctuationService(app)
api.add_resource(StatisticController, '/statistic', resource_class_kwargs={'service': price_fluctuation_service})
