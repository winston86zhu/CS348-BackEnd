from flask import request, jsonify
from flask_restful import Resource

from .models import User, Client, Supplier, Planner
from .managers import UserManager


class UserResource(Resource):
    @staticmethod
    def get():

        #user?type=client
        user_type = request.args.get('type',1)
        manager = UserManager()

        try:
            if (user_type == "client"):
                result = manager.fetch_from_client()
                for row in result:
                    row.account_balance = float(row.account_balance)
            elif(user_type == "supplier"):
                result = manager.fetch_from_supplier()
            elif(user_type == "planner"):
                result = manager.fetch_from_planner()
                for row in result:
                    row.rate = float(row.rate)
            else:
                pass
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
            user_type = payload['user_type']

            if user_type == 'client':
                account_balance = payload['account_balance']
            elif user_type == 'supplier':
                banking_account = payload['banking_account']
                website_link = payload['website_link']
                contact_email = payload['contact_email']
            elif user_type == 'planner':
                position = payload['position']
                rate = payload['rate']
                banking_account = payload['banking_account']
            else:
                raise KeyError('user_type')
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
            manager.create_user(user)
            result = manager.fetchone()
        except Exception as e:
            response = jsonify({
                'error': 'Internal Error',
                'message': f'Unknown error: {str(e)}'
            })
            response.status_code = 500
            return response

        user_id = result[0]

        try:
            if user_type == 'client':
                client = Client(user_id, first_name, last_name, email, password, account_balance)
                manager.create_client(client)
                result = manager.fetch_client_by_user_id(user_id)
                result.account_balance = float(result.account_balance)
            elif user_type == 'supplier':
                supplier = Supplier(user_id, first_name, last_name, email, password, banking_account, website_link, contact_email)
                manager.create_supplier(supplier)
                result = manager.fetch_supplier_by_user_id(user_id)
            elif user_type == 'planner':
                planner = Planner(user_id, first_name, last_name, email, password, position, rate, banking_account)
                manager.create_planner(planner)
                result = manager.fetch_planner_by_user_id(user_id)
                result.rate = float(result.rate)
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
