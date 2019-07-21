import psycopg2


class DatabaseConnection:
    def __init__(self, db_url):
        global conn, cur

        conn = psycopg2.connect(db_url)
        cur = conn.cursor()

    def rollback(self):
        cur.execute("ROLLBACK")
        conn.commit()

    def execute_write_op(self, query):
        cur.execute(query)
        conn.commit()

    def fetch_single_row(self, query):
        cur.execute(query)
        return cur.fetchone()

    def fetch_all_rows(self, query):
        cur.execute(query)
        return cur.fetchall()

    def fetchone(self):
        return cur.fetchone()
