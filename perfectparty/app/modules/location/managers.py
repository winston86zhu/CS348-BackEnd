from extensions import DatabaseConnection as db_conn
from .models import Location


class LocationManager(db_conn):
    def __init__(self):
        pass

    def deserialize(self, row):
        return Location(*row)

    def fetch_by_id(self, location_id):
        query = f"""
            SELECT *
            FROM Location
            WHERE LocationID = {location_id}
        """

        try:
            result = self.fetch_single_row(query)
        except Exception as e:
            self.rollback()
            raise e

        return self.deserialize(result)

    def create(self, location):
        query = f"""
            INSERT 
            INTO Location (LocationCapacity, LocationOpenHour, LocationCloseHour, LocationName, LocationAddress, LocationPrice)
            VALUES({location.location_capacity}, {location.location_open_hour}, {location.location_close_hour}, '{location.location_name}', '{location.location_address}', {location.location_price});
        """

        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e

    def update(self, location):
        query = f"""
            UPDATE Location
            SET LocationCapacity = '{location.location_capacity}',
                LocationOpenHour = '{location.location_open_hour}',
                LocationCloseHour = '{location.location_close_hour}',
                LocationName = '{location.location_name}',
                LocationAddress = '{location.location_address}',
                LocationPrice = '{location.location_price}'
            WHERE LocationID = {location.location_id};
        """

        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e

    def fetch_all_location(self):
        query = f"""
            SELECT * 
            FROM Location;
        """

        try:
            result = self.fetch_all_rows(query)
        except Exception as e:
            self.rollback()
            raise e

        return list(self.deserialize(row) for row in result)
