from dataclasses import dataclass


@dataclass
class Order:
    item_id: int
    supplier_user_id: int
    client_user_id: int
    event_id: int
    quantity: int
