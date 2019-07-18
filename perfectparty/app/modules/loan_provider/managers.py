from extensions import DatabaseConnection as db_conn
from .models import LP


class LPManager(db_conn):
    def __init__(self):
        pass

    def deserialize(self, row):
        return LP(*row)

    def create(self, user):
        query = f"""
            INSERT 
            INTO Loan_Provider (InstitutionID, PhoneNumber, EmbeddedURL)
            VALUES('{LP.InstitutionID}', '{LP.PhoneNumber}', '{LP.EmbeddedURL}')
        """

        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e

    def fetch_all_LP(self):
        query = f"""
            SELECT * 
            FROM Loan_Provider
        """

        try:
            result = self.fetch_all_rows(query)
        except Exception as e:
            self.rollback()
            raise e

        return self.deserialize(result)
