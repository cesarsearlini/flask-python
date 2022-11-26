# flask-python 

Este reporitorio tem objetivo de criação de uma agenda de contato, para fins educacional.

from flask import Flask
from flask_restful import Resource, Api

app = Flask(_name_)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if _name_ == '_main_':
    app.run(debug=True)
    