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

    def fetch_from_client(self):
        query = f"""
        SELECT UserID, FirstName, LastName, Email, Password, AccountBalance
            FROM "user"
            INNER JOIN client
                ON "user".UserID = client.ClientUserID 
        """
        try:
            result = self.fetch_all_rows(query)
        except Exception as e:
            self.rollback()
            raise e

        return list(self.deserialize(row) for row in result)
    
    def fetch_from_supplier(self):
        query = f"""
        SELECT "user".UserID,"user".FirstName,"user".LastName,"user".Email,
        "user".Password FROM "user" 
        INNER JOIN Supplier 
        ON Supplier.SupplierUserID = "user".UserID; 
        """
        try:
            result = self.fetch_all_rows(query)
        except Exception as e:
            self.rollback()
            raise e

        return list(self.deserialize(row) for row in result)

    def fetch_from_planner(self):
        query = f"""
        SELECT "user".UserID,"user".FirstName,"user".LastName,"user".Email,
        "user".Password FROM "user" 
        INNER JOIN Planner 
        ON PLanner.PlannerUserID = "user".UserID; 
        """
        try:
            result = self.fetch_all_rows(query)
        except Exception as e:
            self.rollback()
            raise e

        return list(self.deserialize(row) for row in result)

