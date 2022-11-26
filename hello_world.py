from notify_service import NotifyService
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class save(Resource):
    def get(self, param):
        InterfaceDataBaseService.save(param)
        notify = NotifyService()
        notify.exec(param)
        return {'Nome informado é ': param}

api.add_resource(HelloWorld, '/p2ptransfer/<string:param>')

if __name__ == '__main__':
    app.run(debug=True)

class InterfaceDataBaseService():
    def save(param):
        #aqui eu salvo no banco e retorno OK
        return