from flask import request, jsonify
from flask_restful import Resource

from .models import Location
from .managers import LocationManager


class LocationResource(Resource):
    @staticmethod
    def get():
        manager = LocationManager()

        try:
            result = manager.fetch_all_location()
        except Exception as e:
            response = jsonify({
                'error': 'Internal Error',
                'message': f'Unknown error: {str(e)}'
            })
            response.status_code = 500
            return response

        for row in result:
            row.location_open_hours = str(row.location_open_hours)

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
            location_capacity = payload['location_capacity']
            location_open_hours = payload['location_open_hours']
            location_name = payload['location_name']
            location_address = payload['location_address']
            location_price = payload['location_price']
        except KeyError as e:
            response = jsonify({
                'error': 'KeyError',
                'message': f'Missing key {str(e)} from payload'
            })
            response.status_code = 400
            return response

        manager = LocationManager()
        location = Location(-1, location_capacity, location_open_hours, location_name, location_address, location_price)

        try:
            manager.create(location)
        except Exception as e:
            response = jsonify({
                'error': 'Internal Error',
                'message': f'Unknown error: {str(e)}'
            })
            response.status_code = 500
            return response

        try:
            result = manager.fetch_all_location()
        except Exception as e:
            response = jsonify({
                'error': 'Internal Error',
                'message': f'Unknown error: {str(e)}'
            })
            response.status_code = 500
            return response

        for row in result:
            row.location_open_hours = str(row.location_open_hours)
        
        response = jsonify(result)
        response.status_code = 201
        return response
