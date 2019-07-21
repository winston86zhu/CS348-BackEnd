from dataclasses import dataclass


@dataclass
class Planner:
    user_id: int
    Position: str
    Rate: int
    BankingAccount: str
