from extensions import DatabaseConnection as db_conn
from .models import Flower, Food, Music


class UserManager(db_conn):
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
            VALUES('{supply.ItemPrice}', '{supply.ItemName}')
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
            INTO Music (Genre, Artist)
            VALUES ({supply.Genre}, {supply.Artist})
        """

        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e

    def create_supplier(self, supplier):
        query = f"""
            INSERT
            INTO supplier (SupplierUserID, BankingAccount, WebsiteLink, ContactEmail)
            VALUES ({supplier.user_id}, '{supplier.banking_account}', '{supplier.website_link}', '{supplier.contact_email}')
        """

        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e

    def create_planner(self, planner):
        query = f"""
            INSERT
            INTO planner (PlannerUserID, Position, Rate, BankingAccount)
            VALUES ({planner.user_id}, '{planner.position}', {planner.rate}, '{planner.banking_account}')
        """

        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e

    def fetch_client_by_user_id(self, user_id):
        query = f"""
            SELECT UserID, FirstName, LastName, Email, Password, AccountBalance
            FROM "user"
            INNER JOIN client
                ON "user".UserID = client.ClientUserID 
            WHERE UserID={user_id}
        """

        try:
            result = self.fetch_single_row(query)
        except Exception as e:
            self.rollback()
            raise e

        return self.deserialize_client(result)

    def fetch_supplier_by_user_id(self, user_id):
        query = f"""
            SELECT UserID, FirstName, LastName, Email, Password, BankingAccount, WebsiteLink, ContactEmail
            FROM "user"
            INNER JOIN supplier
                ON "user".UserID = supplier.SupplierUserID 
            WHERE UserID={user_id}
        """

        try:
            result = self.fetch_single_row(query)
        except Exception as e:
            self.rollback()
            raise e

        return self.deserialize_supplier(result)

    def fetch_planner_by_user_id(self, user_id):
        query = f"""
            SELECT UserID, FirstName, LastName, Email, Password, Position, Rate, BankingAccount
            FROM "user"
            INNER JOIN planner
                ON "user".UserID = planner.PlannerUserID 
            WHERE UserID={user_id}
        """

        try:
            result = self.fetch_single_row(query)
        except Exception as e:
            self.rollback()
            raise e

        return self.deserialize_planner(result)

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

        return list(self.deserialize_client(row) for row in result)
    
    def fetch_from_supplier(self):
        query = f"""
        SELECT UserID, FirstName, LastName, Email, Password, BankingAccount, WebsiteLink, ContactEmail
        FROM "user"
        INNER JOIN supplier
            ON "user".UserID = supplier.SupplierUserID
        """
        try:
            result = self.fetch_all_rows(query)
        except Exception as e:
            self.rollback()
            raise e

        return list(self.deserialize_supplier(row) for row in result)

    def fetch_from_planner(self):
        query = f"""
        SELECT UserID, FirstName, LastName, Email, Password, Position, Rate, BankingAccount
        FROM "user"
        INNER JOIN planner
            ON "user".UserID = planner.PlannerUserID 
        """
        try:
            result = self.fetch_all_rows(query)
        except Exception as e:
            self.rollback()
            raise e

        return list(self.deserialize_planner(row) for row in result)
