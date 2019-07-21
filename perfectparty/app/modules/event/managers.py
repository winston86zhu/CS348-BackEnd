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
            );
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

    def fetch_by_clientid(self, client_id):
        query = f"""
            SELECT * 
            FROM Event
            WHERE ClientUserID={client_id}
        """

        try:
            result = self.fetch_all_rows(query)
        except Exception as e:
            self.rollback()
            raise e

        return list(self.deserialize(row) for row in result)
