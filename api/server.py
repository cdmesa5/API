from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers.Predios import Predio

app = Flask(__name__)
CORS(app)

@app.route('/predios',methods=['GET'])
def getAll():
    print("predios get")
    return (Predio.list())

@app.route('/predios',methods=['POST'])
def postOne():
    print("predios post")
    body = request.json
    return (Predio.create(body))
