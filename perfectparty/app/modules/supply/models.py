from dataclasses import dataclass


@dataclass
class Supply:
    item_id: int
    ItemPrice: float
    ItemName: str
    supplier_id: int
    quantity: int
    


@dataclass
class Flower(Supply):
    flower_color: str
    supplier_id: int
    quantity: int


@dataclass
class Music(Supply):
    genre: str
    artist: str
    supplier_id: int
    quantity: int


@dataclass
class Food(Supply):
    FoodType: str
    FoodIngredients: str
    supplier_id: int
    quantity: int

# @dataclass
# class ProvidedBy(Supply):
#     supplier_id: int
#     quantity: int

