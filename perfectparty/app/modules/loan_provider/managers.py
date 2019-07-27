from extensions import DatabaseConnection as db_conn
from .models import LoanProvider


class LoanProviderManager(db_conn):
    def __init__(self):
        pass

    def deserialize(self, row):
        return LoanProvider(*row)

    def create(self, loan_provider):
        query = f"""
            INSERT 
            INTO Loan_Provider (Name, PhoneNumber, EmbeddedURL)
            VALUES('{loan_provider.name}', {loan_provider.phone_number}, '{loan_provider.embedded_url}');
        """

        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e

    def fetch_all_providers(self):
        query = f"""
            SELECT *
            FROM Loan_Provider;
        """

        try:
            result = self.fetch_all_rows(query)
        except Exception as e:
            self.rollback()
            raise e

        return list(self.deserialize(row) for row in result)
