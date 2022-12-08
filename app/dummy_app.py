from flask import Flask
from flask_restful import Api

from app.resource.dummy import dummy_resource
from app.resource.health_check import health_resource

app = Flask(__name__)
api = Api(app)

health_resource(api)
dummy_resource(api)