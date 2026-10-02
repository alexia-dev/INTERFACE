from __future__ import annotations


def parse_decimal_amount(value: str) -> int | None:
    normalized = value.strip().replace("R$", "").replace(" ", "").replace(".", "").replace(",", ".")
    try:
        amount = float(normalized)
    except ValueError:
        return None
    if amount < 0:
        return None
    return round(amount * 100)


def format_brl(cents: int) -> str:
    return f"R$ {cents / 100:.2f}".replace(".", ",")
