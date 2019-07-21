from dataclasses import dataclass


@dataclass
class Location:
    LocationID: int
    LocationCapacity: int
    LocationOpenHours: str
    LocationName: str
    LocationAddress: str
    LocationPrice: int
