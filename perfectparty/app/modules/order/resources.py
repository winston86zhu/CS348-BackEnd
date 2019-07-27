from flask import request, jsonify
from flask_restful import Resource

from .models import Order
from .managers import OrderManager


class OrderResource(Resource):
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
            item_id = payload['item_id']
            client_user_id = payload['client_user_id']
            supplier_user_id = payload['supplier_user_id']
            event_id = payload['event_id']
            quantity = payload['quantity']
        except KeyError as e:
            response = jsonify({
                'error': 'KeyError',
                'message': f'Missing key {str(e)} from payload'
            })
            response.status_code = 400
            return response

        manager = OrderManager()
        order = Order(item_id, supplier_user_id, client_user_id, event_id, quantity)

        try:
            manager.create(order)
        except Exception as e:
            response = jsonify({
                'error': 'Internal Error',
                'message': f'Unknown error: {str(e)}'
            })
            response.status_code = 500
            return response

        try:
            result = manager.fetch_by_itemid_and_eventid(order.item_id, order.event_id)
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

    @staticmethod
    def delete():
        payload = request.get_json()

        try:
            item_id = payload['item_id']
            supplier_user_id = payload['supplier_user_id']
            client_user_id = payload['client_user_id']
            event_id = payload['event_id']
        except KeyError as e:
            response = jsonify({
                'error': 'KeyError',
                'message': f'Missing key {str(e)} from payload'
            })
            response.status_code = 400
            return response

        manager = OrderManager()

        try:
            manager.delete(item_id, supplier_user_id, client_user_id, event_id)
        except Exception as e:
            response = jsonify({
                'error': 'Internal Error',
                'message': f'Unknown error: {str(e)}'
            })
            response.status_code = 500
            return response

        return '', 204