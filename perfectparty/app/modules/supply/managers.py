from extensions import DatabaseConnection as db_conn
from .models import Flower, Food, Music


class SuppplyManager(db_conn):
    def __init__(self):
        pass

    def deserialize_music(self, row):
        return Music(*row)

    def deserialize_food(self, row):
        return Food(*row)

    def deserialize_flower(self, row):
        return Flower(*row)

    def create_supply(self, supply):
        query = f"""
            INSERT 
            INTO Supply (ItemPrice, ItemName)
            VALUES({supply.ItemPrice}, '{supply.ItemName}')
            RETURNING ItemId
        """

        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e

    def create_music(self, supply):
        query = f"""
            INSERT
            INTO Music (ItemId, Genre, Artist)
            VALUES ({supply.item_id},'{supply.genre}', '{supply.artist}')
        """

        query2 = f"""
            INSERT
            INTO ProvidedBy (ItemId, SupplierUserID, Quantity)
            VALUES ({supply.item_id},{supply.supplier_user_id}, {supply.quantity})
        """

        try:
            self.execute_write_op(query)
            self.execute_write_op(query2)
        except Exception as e:
            self.rollback()
            raise e

    def create_flower(self, flower):
        query = f"""
            INSERT
            INTO Flower (ItemId, FlowerColor)
            VALUES ({flower.item_id},'{flower.flower_color}')
        """

        query2 = f"""
            INSERT
            INTO ProvidedBy (ItemId, SupplierUserID, Quantity)
            VALUES ({flower.item_id},{flower.supplier_user_id}, {flower.quantity})
        """

        try:
            self.execute_write_op(query)
            self.execute_write_op(query2)
        except Exception as e:
            self.rollback()
            raise e

    def create_food(self, food):
        query = f"""
            INSERT
            INTO Food (ItemId,FoodType, FoodIngredients)
            VALUES ({food.item_id}, '{food.FoodType}', '{food.FoodIngredients}')
        """

        query2 = f"""
            INSERT
            INTO ProvidedBy (ItemId, SupplierUserID, Quantity)
            VALUES ({food.item_id},{food.supplier_user_id}, {food.quantity})
        """

        try:
            self.execute_write_op(query)
            self.execute_write_op(query2)
        except Exception as e:
            self.rollback()
            raise e

    def fetch_music_by_item_id(self, item_id):
        query = f"""
            SELECT Supply.ItemId, ItemPrice, ItemName, Genre, Artist, SupplierUserID, Quantity
            FROM Supply
            INNER JOIN Music
                ON Music.ItemId = Supply.ItemId 
            INNER JOIN ProvidedBy
                ON ProvidedBy.ItemId = Supply.ItemId 
            WHERE Supply.ItemId={item_id}
        """

        try:
            result = self.fetch_single_row(query)
        except Exception as e:
            self.rollback()
            raise e

        return self.deserialize_music(result)

    def fetch_flower_by_item_id(self, item_id):
        query = f"""
            SELECT Flower.ItemId, ItemPrice, ItemName, FlowerColor, SupplierUserID, Quantity
            FROM Supply
            INNER JOIN Flower
                ON Supply.ItemId = Flower.ItemId 
            INNER JOIN ProvidedBy
                ON ProvidedBy.ItemId = Supply.ItemId
            WHERE Supply.ItemId={item_id}
        """

        try:
            result = self.fetch_single_row(query)
        except Exception as e:
            self.rollback()
            raise e

        return self.deserialize_flower(result)

    def fetch_food_by_item_id(self, item_id):
        query = f"""
            SELECT Supply.ItemId,ItemPrice, ItemName, FoodType,FoodIngredients, SupplierUserID, Quantity
            FROM Supply
            INNER JOIN Food
                ON Supply.ItemId = Food.ItemId 
            INNER JOIN ProvidedBy
                ON ProvidedBy.ItemId = Supply.ItemId 
            WHERE Supply.ItemId={item_id}
        """

        try:
            result = self.fetch_single_row(query)
        except Exception as e:
            self.rollback()
            raise e

        return self.deserialize_food(result)

    def fetch_from_music(self):
        query = f"""
            SELECT Supply.ItemId, ItemPrice, ItemName, Genre, Artist, SupplierUserID, Quantity
            FROM Supply
            INNER JOIN Music
                ON Music.ItemId = Supply.ItemId 
            INNER JOIN ProvidedBy
                ON ProvidedBy.ItemId = Supply.ItemId
        """

        try:
            result = self.fetch_all_rows(query)
        except Exception as e:
            self.rollback()
            raise e

        return list(self.deserialize_music(row) for row in result)
    
    def fetch_from_flower(self):
        query = f"""
            SELECT Flower.ItemId, ItemPrice, ItemName, FlowerColor, SupplierUserID, Quantity
            FROM Supply
            INNER JOIN Flower
                ON Supply.ItemId = Flower.ItemId 
            INNER JOIN ProvidedBy
                ON ProvidedBy.ItemId = Supply.ItemId
        """

        try:
            result = self.fetch_all_rows(query)
        except Exception as e:
            self.rollback()
            raise e

        return list(self.deserialize_flower(row) for row in result)

    def fetch_from_food(self):
        query = f"""
            SELECT Supply.ItemId,ItemPrice, ItemName, FoodType,FoodIngredients, SupplierUserID, Quantity
            FROM Supply
            INNER JOIN Food
                ON Supply.ItemId = Food.ItemId 
            INNER JOIN ProvidedBy
                ON ProvidedBy.ItemId = Supply.ItemId 
        """
        try:
            result = self.fetch_all_rows(query)
        except Exception as e:
            self.rollback()
            raise e

        return list(self.deserialize_food(row) for row in result)
    
    def update_flower(self, flower):
        query = f"""
            UPDATE flower
            SET FlowerColor = '{flower.flower_color}'
            WHERE ItemId = {flower.ItemId}
        """

        query2 = f"""
            UPDATE ProvidedBy
            SET SupplierUserID = '{flower.supplier_user_id}',
                Quantity = '{flower.quantity}'
            WHERE ItemId = {flower.ItemId}
        """
        try:
            self.execute_write_op(query)
            self.execute_write_op(query2)
        except Exception as e:
            self.rollback()
            raise e

    def update_music(self, music):
        query = f"""
            UPDATE music
            SET Genre = '{music.genre}',
             Artist = '{music.artist}'
            WHERE ItemId = {music.item_id}
        """

        query2 = f"""
            UPDATE ProvidedBy
            SET SupplierUserID = '{music.supplier_user_id}',
                Quantity = '{music.quantity}'
            WHERE ItemId = {music.ItemId}
        """
        try:
            self.execute_write_op(query)
            self.execute_write_op(query2)
        except Exception as e:
            self.rollback()
            raise e

    def update_food(self, food):
        query = f"""
            UPDATE food
            SET FoodType = '{food.FoodType}',
             FoodIngredients = '{food.FoodIngredients}'
            WHERE ItemId = {food.item_id}
        """

        query2 = f"""
            UPDATE ProvidedBy
            SET SupplierUserID = '{food.supplier_user_id}',
                Quantity = '{food.quantity}'
            WHERE ItemId = {food.ItemId}
        """
        try:
            self.execute_write_op(query)
            self.execute_write_op(query2)
        except Exception as e:
            self.rollback()
            raise e

    def update_supply(self, supply):
        query = f"""
            UPDATE supply
            SET ItemPrice = {supply.ItemPrice},
                ItemName = '{supply.ItemName}'
            WHERE ItemId = {supply.item_id}
        """

        query2 = f"""
            UPDATE ProvidedBy
            SET SupplierUserID = '{supply.supplier_user_id}',
                Quantity = '{supply.quantity}'
            WHERE ItemId = {supply.ItemId}
        """
        try:
            self.execute_write_op(query)
            self.execute_write_op(query2)
        except Exception as e:
            self.rollback()
            raise e
