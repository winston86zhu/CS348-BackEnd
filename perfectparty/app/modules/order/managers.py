from extensions import DatabaseConnection as db_conn
from .models import Order


class OrderManager(db_conn):
    def __init__(self):
        pass

    def deserialize(self, row):
        return Order(*row)

    def create(self, order):
        query = f"""
            INSERT 
            INTO "order" (ItemID, SupplierUserID, ClientUserID, EventID, Quantity)
            VALUES({order.item_id}, {order.supplier_user_id}, {order.client_user_id}, {order.event_id}, {order.quantity});
        """

        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e

    def delete(self, item_id, supplier_user_id, client_user_id, event_id):
        query = f"""
            DELETE FROM "order"
            WHERE ItemID = {item_id} AND SupplierUserID = {supplier_user_id} AND ClientUserID = {client_user_id} AND EventID = {event_id};
        """

        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e

    def fetch_by_itemid(self, item_id):
        query = f"""
            SELECT * 
            FROM "order"
            WHERE ItemID={item_id};
        """

        try:
            result = self.fetch_all_rows(query)
        except Exception as e:
            self.rollback()
            raise e

        return list(self.deserialize(row) for row in result)

    def fetch_by_clientid(self, client_id):
        query = f"""
            SELECT * 
            FROM "order"
            WHERE ClientUserID={client_id};
        """

        try:
            result = self.fetch_all_rows(query)
        except Exception as e:
            self.rollback()
            raise e

        return list(self.deserialize(row) for row in result)

    def fetch_by_supplierid(self, supplier_user_id):
        query = f"""
            SELECT * 
            FROM "order"
            WHERE SupplierUserID={supplier_user_id};
        """

        try:
            result = self.fetch_all_rows(query)
        except Exception as e:
            self.rollback()
            raise e

        return list(self.deserialize(row) for row in result)

    def fetch_by_eventid(self, event_id):
        query = f"""
            SELECT * 
            FROM "order"
            WHERE EventID={event_id};
        """

        try:
            result = self.fetch_all_rows(query)
        except Exception as e:
            self.rollback()
            raise e

        return list(self.deserialize(row) for row in result)

    def fetch_by_itemid_and_eventid(self, item_id, event_id):
        query = f"""
            SELECT * 
            FROM "order"
            WHERE ItemID={item_id} AND EventID={event_id};
        """

        try:
            result = self.fetch_single_row(query)
        except Exception as e:
            self.rollback()
            raise e

        return self.deserialize(result)