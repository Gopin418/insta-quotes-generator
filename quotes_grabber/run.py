try:
    from flask import Flask
    from flask_restful import Resource, Api
    import sys
    import os
except Exception as e:
    print(f"Error : {e}")

app = Flask(__name__)
api = Api(app)


class ApiController(Resource):
    def __init__(self):
        pass

    def get(self):
        message = "Hello from Flask REST API!, this is GET Method using API Resource Controller"

        return message


api.add_resource(ApiController, '/')

if __name__ == "main":
    app.run(debug=True, host='0.0.0.0')
