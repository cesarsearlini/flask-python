from flask_restful import Resource

from ..util.logz import create_logger


class BaseResource(Resource):

    def __init__(self):
        self.logger = create_logger()
