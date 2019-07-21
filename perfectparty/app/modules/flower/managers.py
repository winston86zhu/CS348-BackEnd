from extensions import DatabaseConnection as db_conn
from .models import Flower


class FlowerManager(db_conn):
    def __init__(self):
        pass

    def deserialize(self, row):
        return Flower(*row)

    def create(self, flower):
        query = f"""
            INSERT 
            INTO Flower (FlowerColor)
            VALUES('{flower.f_color}');
        """

        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e

    def fetch_all_flower(self):
        query = f"""
            SELECT * 
            FROM Flower;
        """

        try:
            result = self.fetch_all_rows(query)
        except Exception as e:
            self.rollback()
            raise e

        return list(self.deserialize(row) for row in result)
