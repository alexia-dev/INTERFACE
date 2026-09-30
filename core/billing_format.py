from __future__ import annotations


def parse_brl_to_cents(value: str) -> int | None:
    normalized = value.strip().replace("R$", "").replace(" ", "")
    normalized = normalized.replace(".", "").replace(",", ".")
    try:
        amount = float(normalized)
    except ValueError:
        return None
    if amount < 0:
        return None
    return round(amount * 100)


def format_brl(cents: int) -> str:
    return f"R$ {cents / 100:.2f}".replace(".", ",")
