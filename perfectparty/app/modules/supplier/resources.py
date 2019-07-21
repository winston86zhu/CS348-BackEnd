from flask import request, jsonify
from flask_restful import Resource

from .models import Supplier
from .managers import SupplierManager


class SupplierResource(Resource):
    @staticmethod
    def get():
        """
        Show all Suppliers
        """
        manager = SupplierManager()
        try:
            result = manager.fetch_all_supplier()
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
