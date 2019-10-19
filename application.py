from predictor import EnsembleBuilder
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def starter():
        return {"Use" : "/predict"}

@app.route('/predict', methods = ['GET', 'POST'])
def predictor():
        if(request.method == 'POST'):
                rec_json = request.get_json()
                recogspeech = rec_json['speech']
                print(recogspeech)
                eb = EnsembleBuilder()
                result = eb.make_prediction(recogspeech)
                print(result, recogspeech)
                return jsonify({'sentiment' : result, 'speech': recogspeech}), 201





