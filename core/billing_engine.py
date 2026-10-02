from __future__ import annotations

from core.billing_models import BillingContext, PriceRule


class BillingConfigurationError(ValueError):
    pass


def find_applicable_price(context: BillingContext, rules: list[PriceRule]) -> PriceRule:
    candidates = [
        rule for rule in rules
        if rule.active
        and rule.context_type == context.context_type
        and rule.context_id == context.context_id
        and rule.catalog_item_code == context.catalog_item_code
        and rule.modality == context.modality
        and rule.valid_from <= context.service_date
        and (rule.valid_to is None or context.service_date <= rule.valid_to)
    ]
    if not candidates:
        raise BillingConfigurationError("Nenhum valor vigente foi encontrado para o contexto informado.")
    return max(candidates, key=lambda item: item.valid_from)


def calculate_total(context: BillingContext, rules: list[PriceRule]):
    if context.quantity <= 0:
        raise BillingConfigurationError("A quantidade deve ser maior que zero.")
    return find_applicable_price(context, rules).amount * context.quantity
