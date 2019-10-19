from predictor import EnsembleBuilder
from flask import Flask, render_template, url_for, request
from flask_restful import Resource, Api
import os

app = Flask(__name__)
api = Api(app)

class Prediction(Resource):
        def get(self):
                return {'Result':'Its working'}
        
        def post(self):
                rec_json = request.get_json()
                recogspeech = rec_json['speech']
                print(recogspeech)
                eb = EnsembleBuilder()
                result = eb.make_prediction(recogspeech)
                print(result, recogspeech)
                return {'sentiment' : result, 'speech': recogspeech}, 201

api.add_resource(Prediction, '/predict')


if __name__ == '__main__':
    app.run(debug = True)




