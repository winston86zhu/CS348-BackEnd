from flask import request, jsonify
from flask_restful import Resource

from .models import LoanProvider
from .managers import LoanProviderManager


class LoanProviderResource(Resource):
    @staticmethod
    def get():
        manager = LoanProviderManager()

        try:
            result = manager.fetch_all_providers()
        except Exception as e:
            response = jsonify({
                'error': 'Internal Error',
                'message': f'Unknown error: {str(e)}'
            })
            response.status_code = 500
            return response

        response = jsonify(result)
        response.status_code = 200
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
            name = payload['name']
            phone_number = payload['phone_number']
            embedded_url = payload['embedded_url']
        except KeyError as e:
            response = jsonify({
                'error': 'KeyError',
                'message': f'Missing key {str(e)} from payload'
            })
            response.status_code = 400
            return response

        manager = LoanProviderManager()
        loan_provider = LoanProvider(-1, name, phone_number, embedded_url)

        try:
            manager.create(loan_provider)
        except Exception as e:
            response = jsonify({
                'error': 'Internal Error',
                'message': f'Unknown error: {str(e)}'
            })
            response.status_code = 500
            return response

        return '', 204
