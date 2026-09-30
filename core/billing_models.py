from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class PriceRule:
    provider_id: int
    insurer_id: int
    procedure_id: int
    modality: str
    amount: Decimal
    valid_from: date
    valid_to: date | None = None
    active: bool = True


@dataclass(frozen=True, slots=True)
class BillingContext:
    provider_id: int
    insurer_id: int
    procedure_id: int
    modality: str
    service_date: date
    quantity: Decimal = Decimal("1")
