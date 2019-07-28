from extensions import DatabaseConnection as db_conn
from .models import Event


class EventManager(db_conn):
    def __init__(self):
        pass

    def deserialize(self, row):
        return Event(*row)

    def create(self, event):
        query = f"""
            INSERT 
            INTO Event (
                ClientUserID,
                PlannerUserID,
                LocationID,
                InstitutionID,
                EventName,
                EventBudget,
                PlanningFee,
                StartTimestamp,
                EndTimestamp
            )
            VALUES(
                {event.client_user_id},
                {event.planner_user_id},
                {event.location_id},
                {event.institution_id},
                '{event.event_name}',
                {event.event_budget},
                {event.planning_fee},
                '{event.start_timestamp}', 
                '{event.end_timestamp}'
            )
            RETURNING EventID;
        """

        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e

    def update(self, event):
        query = f"""
            UPDATE Event 
            SET ClientUserID = {event.client_user_id},
                PlannerUserID = {event.planner_user_id},
                LocationID = {event.location_id},
                InstitutionID = {event.institution_id},
                EventName = '{event.event_name}',
                EventBudget = {event.event_budget},
                PlanningFee = {event.planning_fee},
                StartTimestamp = '{event.start_timestamp}',
                EndTimestamp = '{event.end_timestamp}'
            WHERE EventID = {event.event_id};
        """

        try:
            self.execute_write_op(query)
        except Exception as e:
            self.rollback()
            raise e

    def fetch_by_eventid(self, event_id):
        query = f"""
            SELECT * 
            FROM Event
            WHERE EventID={event_id};
        """

        try:
            result = self.fetch_single_row(query)
        except Exception as e:
            self.rollback()
            raise e

        return self.deserialize(result)

    def fetch_by_eventid_special(self, event_id):
        event_query = f"""
            SELECT Event.*, Location.LocationName, LocationAddress, "user".FirstName, "user".LastName, Loan_Provider.Name
            FROM Event
                LEFT JOIN Location ON Event.LocationID = Location.LocationID
                LEFT JOIN "user" ON Event.PlannerUserID = "user".UserID
                LEFT JOIN Loan_Provider ON Event.InstitutionID = Loan_Provider.InstitutionID
            WHERE EventID={event_id};
        """

        order_query = f"""
            SELECT "order".*, "user".FirstName, "user".LastName, Supply.ItemName
            FROM "order"
                LEFT JOIN "user" ON "order".SupplierUserID = "user".UserID
                LEFT JOIN Supply ON "order".ItemID = Supply.ItemID
            WHERE EventID = {event_id};
        """

        try:
            event_result = self.fetch_single_row(event_query)
            order_result = self.fetch_all_rows(order_query)
        except Exception as e:
            self.rollback()
            raise e

        return {
            'event_id': event_result[0],
            'client_user_id': event_result[1],
            'planner_user_id': event_result[2],
            'location_id': event_result[3],
            'institution_id': event_result[4],
            'event_name': event_result[5],
            'event_budget': event_result[6],
            'planning_fee': event_result[7],
            'start_timestamp': event_result[8],
            'end_timestamp': event_result[9],
            'location_name': event_result[10],
            'location_address': event_result[11],
            'planner_name': f'{event_result[12]} {event_result[13]}',
            'loan_provider_name': event_result[14],
            'orders': [
                {
                    'item_id': row[0],
                    'supplier_user_id': row[1],
                    'client_user_id': row[2],
                    'quantity': row[4],
                    'supplier_name': f'{row[5]} {row[6]}',
                    'item_name': row[7]
                } for row in order_result
            ]
        }

    def fetch_by_clientid(self, client_id):
        query = f"""
            SELECT e.EventID, e.ClientUserID, e.PlannerUserID, e.LocationID, e.InstitutionID, e.EventName, e.EventBudget, e.PlanningFee, e.StartTimestamp, e.EndTimestamp,
                CASE WHEN o.count is NULL THEN 0 ELSE o.count END AS orders
            FROM (
                SELECT EventID, count(*) AS count
	            FROM "order" 
	            GROUP BY EventID
	        ) o
            RIGHT JOIN (SELECT * FROM event WHERE ClientUserID={client_id}) e
	        ON e.EventID = o.EventID;
        """

        try:
            result = self.fetch_all_rows(query)
        except Exception as e:
            self.rollback()
            raise e

        return list(self.deserialize(row) for row in result)
