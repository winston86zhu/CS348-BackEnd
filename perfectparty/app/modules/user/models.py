
from dataclasses import dataclass


@dataclass
class User:
    user_id: int
    first_name: str
    last_name: str
    email: str
    password: str


@dataclass
class Client(User):
    account_balance: float


@dataclass
class Supplier(User):
    banking_account: str
    website_link: str
    contact_email: str


@dataclass
class Planner(User):
    position: str
    rate: float
    banking_account: str
