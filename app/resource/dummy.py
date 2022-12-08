from flask import jsonify

from .base_resource import BaseResource
from ..model.dummy_model import DummyModel

parser = DummyModel.add_args()


def dummy_resource(api):
    api.add_resource(Dummy, '/dummy/<string:param>')
    api.add_resource(DummyPost, '/dummy')
    api.add_resource(DummyList, '/dummy')
    return api


class Dummy(BaseResource):

    def get(self, param):
        self.logger.info('This is an info and the input parameter is { %s }', param)
        return jsonify(param)

    def put(self, param):
        args = parser.parse_args()
        self.logger.info('This is an info and the input parameter is { %s } and object body is { %s }', param, args)
        return jsonify(args)

    def delete(self, param):
        args = parser.parse_args()
        self.logger.info('This is an info and the input parameter is { %s } and object body is { %s }', param, args)
        return jsonify(args)


class DummyPost(BaseResource):

    def post(self):
        args = parser.parse_args()
        self.logger.info('This is an info and the input object is { %s }', args)
        return jsonify(args)


class DummyList(BaseResource):

    def get(self):
        args = parser.parse_args()
        self.logger.info('This is an info and the input object is { %s }', args)
        return jsonify(args)
