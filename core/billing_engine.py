from __future__ import annotations

from core.billing_models import BillingContext, PriceRule


class BillingConfigurationError(ValueError):
    pass


def find_applicable_price(context: BillingContext, rules: list[PriceRule]) -> PriceRule:
    candidates = [
        rule for rule in rules
        if rule.active
        and rule.provider_id == context.provider_id
        and rule.insurer_id == context.insurer_id
        and rule.procedure_id == context.procedure_id
        and rule.modality == context.modality
        and rule.valid_from <= context.service_date
        and (rule.valid_to is None or context.service_date <= rule.valid_to)
    ]
    if not candidates:
        raise BillingConfigurationError(
            "Nenhum valor vigente foi encontrado para o atendimento."
        )
    return max(candidates, key=lambda item: item.valid_from)


def calculate_total(context: BillingContext, rules: list[PriceRule]):
    if context.quantity <= 0:
        raise BillingConfigurationError("A quantidade deve ser maior que zero.")
    return find_applicable_price(context, rules).amount * context.quantity
