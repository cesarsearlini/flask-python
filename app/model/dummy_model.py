from flask_restful import reqparse


class DummyModel:

    def __init__(self, id, name, task, create_at):
        self.id = id
        self.name = name
        self.task = task
        self.create_at = create_at

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'task': self.task,
            'create_at': self.create_at,
        }

    @staticmethod
    def add_args():
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        parser.add_argument('name')
        parser.add_argument('task')
        parser.add_argument('create_at')
        return parser
