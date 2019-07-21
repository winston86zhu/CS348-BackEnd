from extensions import DatabaseConnection as db_conn
from .models import Food


class FoodManager(db_conn):
    def __init__(self):
        pass

    def deserialize(self, row):
        return Food(*row)

    def create(self, food):
        query = f"""
            INSERT 
            INTO Food (FoodType, FoodIngredients)
            VALUES('{food.food_type}', '{food.food_ingredient}');
        """

        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e

    def fetch_all_food(self):
        query = f"""
            SELECT * 
            FROM Food;
        """

        try:
            result = self.fetch_all_rows(query)
        except Exception as e:
            self.rollback()
            raise e

        return self.deserialize(result)
