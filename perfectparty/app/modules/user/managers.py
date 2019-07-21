from extensions import DatabaseConnection as db_conn
from .models import User


class UserManager(db_conn):
    def __init__(self):
        pass

    def deserialize(self, row):
        return User(*row)

    def create(self, user):
        query = f"""
            INSERT 
            INTO "user" (FirstName, LastName, Email, Password)
            VALUES('{user.first_name}', '{user.last_name}', '{user.email}', '{user.password}')
        """

        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e

    def fetch_by_email(self, email):
        query = f"""
            SELECT * 
            FROM "user" 
            WHERE Email='{email}'
        """

        try:
            result = self.fetch_single_row(query)
        except Exception as e:
            self.rollback()
            raise e

        return self.deserialize(result)
