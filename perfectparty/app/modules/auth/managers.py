from extensions import DatabaseConnection as db_conn


class AuthManager(db_conn):
    def __init__(self):
        pass

    def fetch_id_pw_by_email(self, email):
        query = f"""
            SELECT UserID, Password
            FROM "user"
            WHERE Email='{email}'
        """

        try:
            result = self.fetch_single_row(query)
        except Exception as e:
            self.rollback()
            raise e

        return result
