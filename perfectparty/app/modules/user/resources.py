from flask import request, jsonify
from flask_restful import Resource

from .models import User
from .managers import UserManager


class UserResource(Resource):
    @staticmethod
    def get():
        pass

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
            first_name = payload['firstName']
            last_name = payload['lastName']
            email = payload['email']
            password = payload['password']
        except KeyError as e:
            response = jsonify({
                'error': 'KeyError',
                'message': f'Missing key {str(e)} from payload'
            })
            response.status_code = 400
            return response

        manager = UserManager()
        user = User(-1, first_name, last_name, email, password)

        try:
            manager.create(user)
        except Exception as e:
            response = jsonify({
                'error': 'Internal Error',
                'message': f'Unknown error: {str(e)}'
            })
            response.status_code = 500
            return response

        try:
            result = manager.fetch_by_email(user.email)
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
