from extensions import DatabaseConnection as db_conn
from .models import Music


class MusicManager(db_conn):
    def __init__(self):
        pass

    def deserialize(self, row):
        return Music(*row)

    def create(self, music):
        query = f"""
            INSERT 
            INTO Music (Genre, Artist)
            VALUES('{music.Genre}', '{music.Artist}');
        """

        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e

    def fetch_all_music(self):
        query = f"""
            SELECT * 
            FROM Music;
        """

        try:
            result = self.fetch_all_rows(query)
        except Exception as e:
            self.rollback()
            raise e

        return list(self.deserialize(row) for row in result)
