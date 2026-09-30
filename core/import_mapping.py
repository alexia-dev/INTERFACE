from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ImportMapping:
    source: str
    target: str
    required: bool = False


STANDARD_BILLING_FIELDS = (
    "provider_id",
    "insurer_id",
    "procedure_code",
    "procedure_name",
    "service_date",
    "quantity",
    "modality",
)


def normalize_row(row: dict[str, object], mappings: list[ImportMapping]) -> dict[str, object]:
    normalized = {}
    for mapping in mappings:
        if mapping.source in row:
            normalized[mapping.target] = row[mapping.source]

    missing = [
        mapping.target
        for mapping in mappings
        if mapping.required and mapping.target not in normalized
    ]
    if missing:
        raise ValueError(f"Campos obrigatórios ausentes: {', '.join(missing)}")
    return normalized
