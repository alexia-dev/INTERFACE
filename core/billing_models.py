from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class PriceRule:
    context_type: str
    context_id: str
    catalog_item_code: str
    modality: str
    amount: Decimal
    valid_from: date
    valid_to: date | None = None
    active: bool = True


@dataclass(frozen=True, slots=True)
class BillingContext:
    context_type: str
    context_id: str
    catalog_item_code: str
    modality: str
    service_date: date
    quantity: Decimal = Decimal("1")
