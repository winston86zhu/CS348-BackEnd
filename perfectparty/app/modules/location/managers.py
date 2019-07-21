from extensions import DatabaseConnection as db_conn
from .models import Location


class LocationManager(db_conn):
    def __init__(self):
        pass

    def deserialize(self, row):
        return Location(*row)

    def create(self, location):
        query = f"""
            INSERT 
            INTO Location (LocationCapacity, LocationOpenHours, LocationName, LocationAddress, LocationPrice)
            VALUES({location.LocationCapacity}, {location.LocationOpenHours}, '{location.LocationName}', '{location.LocationAddress}', {location.LocationPrice});
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
