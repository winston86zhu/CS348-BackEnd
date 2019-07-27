from extensions import DatabaseConnection as db_conn
from .models import Client, Supplier, Planner


class UserManager(db_conn):
    def __init__(self):
        pass

    def deserialize_client(self, row):
        return Client(*row)

    def deserialize_supplier(self, row):
        return Supplier(*row)

    def deserialize_planner(self, row):
        return Planner(*row)

    def create_user(self, user):
        query = f"""
            INSERT 
            INTO "user" (FirstName, LastName, Email, Password)
            VALUES('{user.first_name}', '{user.last_name}', '{user.email}', '{user.password}')
            RETURNING UserID
        """

        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e

    def create_client(self, client):
        query = f"""
            INSERT
            INTO client (ClientUserID, AccountBalance)
            VALUES ({client.user_id}, {client.account_balance})
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

    def update_user(self, user):
        query = f"""
            UPDATE "user"
            SET FirstName = '{user.first_name}',
                LastName = '{user.last_name}',
                Email = '{user.email}',
                Password = '{user.password}'
            WHERE UserID = {user.user_id}
        """
        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e

    def update_client(self, user):
        query = f"""
            UPDATE Client
            SET AccountBalance = {user.account_balance}
            WHERE ClientUserID = {user.user_id}
        """
        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e

    def update_supplier(self, user):
        query = f"""
            UPDATE supplier
            SET BankingAccount = '{user.banking_account}',
                WebsiteLink = '{user.website_link}',
                ContactEmail ='{user.contact_email}'
            WHERE SupplierUserID = {user.user_id}
        """
        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e

    def update_planner(self, user):
        query = f"""
            UPDATE Planner
            SET Position = '{user.position}',
                Rate = {user.rate},
                BankingAccount ='{user.contact_email}'
            WHERE PlannerUserID = {user.banking_account}
        """
        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e

