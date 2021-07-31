from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)


@app.route('/api/hello', methods=['GET'])
def hello_world():
    response = jsonify(message='Hello, World')
    # response.headers.add("Access-Control-Allow-Origin", "*")

    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')
