from dataclasses import dataclass


@dataclass
class Food:
    food_id: int
    food_type: str
    food_ingredient: str
