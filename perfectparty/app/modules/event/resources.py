from flask import request, jsonify
from flask_restful import Resource

from .models import Event
from .managers import EventManager


class EventResource(Resource):
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
            client_user_id = payload['client_user_id']
            planner_user_id = payload.get('planner_user_id', "null")
            location_id = payload.get('location_id', "null")
            institution_id = payload.get('institution_id', "null")
            event_name = payload['event_name']
            event_budget = payload.get('event_budget', 0)
            planning_fee = payload.get('planning_fee', 0)
            start_timestamp = payload['start_timestamp']
            end_timestamp = payload['end_timestamp']
        except KeyError as e:
            response = jsonify({
                'error': 'KeyError',
                'message': f'Missing key {str(e)} from payload'
            })
            response.status_code = 400
            return response

        manager = EventManager()
        event = Event(
            -1,
            client_user_id,
            planner_user_id,
            location_id,
            institution_id,
            event_name,
            event_budget,
            planning_fee,
            start_timestamp,
            end_timestamp
        )

        try:
            manager.create(event)
        except Exception as e:
            response = jsonify({
                'error': 'Internal Error',
                'message': f'Unknown error: {str(e)}'
            })
            response.status_code = 500
            return response

        try:
            # TODO: this needs to be fixed... should fetch the recently created event instead of all
            result = manager.fetch_by_clientid(event.client_user_id)
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
