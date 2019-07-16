from flask_restful import Resource


class User(Resource):
    @staticmethod
    def get():
        return {'hello': 'world'}
