from extensions import DatabaseConnection as db_conn
from .models import Planner


class PlannerManager(db_conn):
    def __init__(self):
        pass

    def deserialize(self, row):
        return Planner(*row)

    def create(self, planner):
        query = f"""
            INSERT 
            INTO Planner (Position, Rate, BankingAccount)
            VALUES('{planner.Position}', {planner.Rate},
             '{planner.BankingAccount}');
        """

        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e

    def fetch_all_planner(self):
        query = f"""
            SELECT * 
            FROM Planner;
        """

        try:
            result = self.fetch_all_rows(query)
        except Exception as e:
            self.rollback()
            raise e

        return list(self.deserialize(row) for row in result)
