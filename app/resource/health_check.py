from flask import jsonify

from .base_resource import BaseResource


def health_resource(api):
    return api.add_resource(HealthCheck, '/health')


class HealthCheck(BaseResource):

    def get(self):
        message_response = 'UP'
        self.logger.info(message_response)
        return jsonify(message_response)
