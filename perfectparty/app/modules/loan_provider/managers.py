from extensions import DatabaseConnection as db_conn
from .models import LP


class LPManager(db_conn):
    def __init__(self):
        pass

    def deserialize(self, row):
        return LP(*row)

    def create(self, lp):
        query = f"""
            INSERT 
            INTO Loan_Provider (Loan_ProviderName, PhoneNumber, EmbeddedURL)
            VALUES ('{lp.Loan_ProviderName}',
            '{lp.PhoneNumber}', '{lp.EmbeddedURL}')
        """

        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e
    
    def fetch_by_id(self, lp_id):
        query = f"""
            SELECT * 
            FROM Loan_Provider 
            WHERE InstitutionID='{lp_id}'
        """
        try:
            result = self.fetch_single_row(query)
        except Exception as e:
            self.rollback()
            raise e

        return self.deserialize(result)

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
