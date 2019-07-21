from extensions import DatabaseConnection as db_conn
from .models import Supplier


class SupplierManager(db_conn):
    def __init__(self):
        pass

    def deserialize(self, row):
        return Supplier(*row)

    def create(self, supplier):
        query = f"""
            INSERT 
            INTO Supplier (AccountBalance)
            VALUES('{supplier.AccountBalance}');
        """

        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e

    def fetch_all_supplier(self):
        query = f"""
            SELECT * 
            FROM Supplier;
        """

        try:
            result = self.fetch_all_rows(query)
        except Exception as e:
            self.rollback()
            raise e

        return list(self.deserialize(row) for row in result)
