from flask import request, jsonify
from flask_restful import Resource

from .models import LP
from .managers import LPManager


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
            #institution_id = payload['InstitutionID']
            phone_number = payload['PhoneNumber']
            lp_name = payload['Loan_ProviderName']
            url = payload['EmbeddedURL']
        except KeyError as e:
            response = jsonify({
                'error': 'KeyError',
                'message': f'Missing key {str(e)} from payload'
            })
            response.status_code = 400
            return response

        manager = LPManager()
        lp = LP(-1,lp_name, phone_number,url)

        try:
            manager.create(lp)
        except Exception as e:
            response = jsonify({
                'error': 'Internal Error',
                'message': f'Unknown error: {str(e)}'
            })
            response.status_code = 500
            return response

        try:
            result = manager.fetch_by_id(lp.InstitutionID)
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
