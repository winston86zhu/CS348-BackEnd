from flask import request, jsonify
from flask_restful import Resource

from .models import Flower
from .managers import FlowerManager


class FlowerResource(Resource):
    @staticmethod
    def get():
        """
        Show all Flowers
        """
        manager = FlowerManager()
        try:
            result = manager.fetch_all_flower()
        except Exception as e:
            response = jsonify({
                'error': 'Internal Error',
                'message': f'Unknown error: {str(e)}'
            })
            response.status_code = 600
            return response
        response = jsonify(result)
        response.status_code = 201
        return response

    @staticmethod
    def post():
        payload = request.get_json()

        if not payload:
            response = jsonify({
                'error': 'Bad Format',
                'message': 'Unable to parse payload'
            })
            response.status_code = 400
            return response

        try:
            f_color = payload['f_color']
        except KeyError as e:
            response = jsonify({
                'error': 'KeyError',
                'message': f'Missing key {str(e)} from payload'
            })
            response.status_code = 400
            return response

        manager = FlowerManager()
        flower = Flower(-1, f_color)

        try:
            manager.create(flower)
        except Exception as e:
            response = jsonify({
                'error': 'Internal Error',
                'message': f'Unknown error: {str(e)}'
            })
            response.status_code = 500
            return response

        try:
            result = manager.fetch_all_flower()
        except Exception as e:
            response = jsonify({
                'error': 'Internal Error',
                'message': f'Unknown error: {str(e)}'
            })
            response.status_code = 500
            return response

        response = jsonify(result)
        response.status_code = 201
        return response
