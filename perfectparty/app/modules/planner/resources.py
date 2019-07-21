from flask import request, jsonify
from flask_restful import Resource

from .models import Planner
from .managers import PlannerManager


class PlannerResource(Resource):
    @staticmethod
    def get():
        """
        Show all Planners
        """
        manager = PlannerManager()
        try:
            result = manager.fetch_all_planner()
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
        pass
