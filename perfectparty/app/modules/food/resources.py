from flask import request, jsonify
from flask_restful import Resource

from .models import Food
from .managers import FoodManager


class FoodResource(Resource):
    @staticmethod
    def get():
        """
        Show all Foods
        """
        manager = FoodManager()
        try:
            result = manager.fetch_all_food()
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
            food_type = payload['food_type']
            food_ingredient = payload['food_ingredient']
        except KeyError as e:
            response = jsonify({
                'error': 'KeyError',
                'message': f'Missing key {str(e)} from payload'
            })
            response.status_code = 400
            return response

        manager = FoodManager()
        food = Food(-1, food_type, food_ingredient)

        try:
            manager.create(food)
        except Exception as e:
            response = jsonify({
                'error': 'Internal Error',
                'message': f'Unknown error: {str(e)}'
            })
            response.status_code = 500
            return response

        try:
            result = manager.fetch_all_food()
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
