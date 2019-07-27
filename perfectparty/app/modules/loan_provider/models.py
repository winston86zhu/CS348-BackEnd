from dataclasses import dataclass


@dataclass
class LoanProvider:
    loan_provider_id: int
    name: str
    phone_number: int
    embedded_url: str
