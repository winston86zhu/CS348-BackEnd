from flask import request, jsonify
from flask_restful import Resource

from .models import Supply, Flower, Food, Music
from .managers import SuppplyManager


class SupplyResource(Resource):
    @staticmethod
    def get():

        #supply?type=music
        user_type = request.args.get('type',1)
        manager = SuppplyManager()

        try:
            if (user_type == "flower"):
                result = manager.fetch_from_flower()
                # for row in result:
                #     row.ItemPrice = float(row.ItemPrice)
            elif(user_type == "food"):
                result = manager.fetch_from_food()
                # for row in result:
                #     row.ItemPrice = float(row.ItemPrice)
            elif(user_type == "music"):
                result = manager.fetch_from_music()
                # for row in result:
                #     row.ItemPrice = float(row.ItemPrice)
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
            item_id = payload['item_id']
            ItemPrice = payload['ItemPrice']
            ItemName = payload['ItemName']
            user_type = payload['supply_type']

            if user_type == 'flower':
                flower_color = payload['flower_color']
            elif user_type == 'music':
                genre = payload['genre']
                artist = payload['artist']
            elif user_type == 'food':
                FoodType = payload['FoodType']
                FoodIngredients = payload['FoodIngredients']
            else:
                raise KeyError('supply_type')
        except KeyError as e:
            response = jsonify({
                'error': 'KeyError',
                'message': f'Missing key {str(e)} from payload'
            })
            response.status_code = 400
            return response

        manager = SuppplyManager()
        supply = Supply(-1, first_name, last_name, email, password)

        try:
            supply.create_supply(supply)
            result = manager.fetchone()
        except Exception as e:
            response = jsonify({
                'error': 'Internal Error',
                'message': f'Unknown error: {str(e)}'
            })
            response.status_code = 500
            return response

        item_id = result[0]

        try:
            if user_type == 'flower':
                flower = Flower(item_id, ItemPrice, ItemName, flower_color)
                manager.create_flower(flower)
                result = manager.fetch_flower_by_item_id(item_id)
                result.ItemPrice = float(result.ItemPrice)
            elif user_type == 'music':
                music = Music(item_id, ItemPrice, ItemName, genre, artist)
                manager.create_music(music)
                result = manager.fetch_music_by_item_id(item_id)
            elif user_type == 'food':
                food = Food(item_id, ItemPrice, ItemName,FoodType,FoodIngredients);
                manager.create_food(food)
                result = manager.fetch_food_by_item_id(item_id)
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
