from dataclasses import dataclass


@dataclass
class Event:
    event_id: int
    client_user_id: int
    planner_user_id: int
    location_id: int
    institution_id: int
    event_name: str
    event_budget: int
    planning_fee: int
    start_timestamp: str
    end_timestamp: str
    orders: int = 0
