from dataclasses import dataclass


@dataclass
class Location:
    location_id: int
    location_capacity: int
    location_open_hours: str
    location_name: str
    location_address: str
    location_price: int
