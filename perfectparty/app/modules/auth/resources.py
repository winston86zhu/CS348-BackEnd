from flask import request, jsonify
from flask_restful import Resource

from .managers import AuthManager


class AuthResource(Resource):
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
            email = payload['email']
            password = payload['password']
        except KeyError as e:
            response = jsonify({
                'error': 'KeyError',
                'message': f'Missing key {str(e)} from payload'
            })
            response.status_code = 400
            return response

        manager = AuthManager()

        try:
            result = manager.fetch_id_pw_by_email(email)
        except Exception as e:
            response = jsonify({
                'error': 'Internal Error',
                'message': f'Unknown error: {str(e)}'
            })
            response.status_code = 500
            return response

        if not result:
            response = jsonify({
                'error': 'Invalid Email',
                'message': 'A user with that email does not exist'
            })
            response.status_code = 400
            return response

        if result[1] != password:
            response = jsonify({
                'error': 'Invalid Password',
                'message': 'Provided password does not match what exists on DB'
            })
            response.status_code = 401
            return response

        response = jsonify({'user_id': result[0]})
        response.status_code = 200
        return response
