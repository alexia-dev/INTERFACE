from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


@dataclass(frozen=True)
class AiRequest:
    message: str
    context: dict[str, Any]
    allowed_tools: tuple[str, ...]


@dataclass(frozen=True)
class AiDecision:
    text: str
    intent: str
    tool: str | None = None
    arguments: dict[str, Any] | None = None
    requires_confirmation: bool = False


class AiProvider(Protocol):
    def decide(self, request: AiRequest) -> AiDecision: ...


class MockAiProvider:
    """Deterministic provider used locally and in tests; replaceable by a real LLM adapter."""
    def decide(self, request: AiRequest) -> AiDecision:
        q=request.message.lower()
        if any(x in q for x in ("pendente", "atenção", "atencao", "resumo")):
            return AiDecision("Vou analisar os dados operacionais disponíveis.", "ANALYZE", "summary")
        if any(x in q for x in ("faturamento", "lançamento", "lancamento", "cobrança", "cobranca")):
            return AiDecision("Vou consultar os lançamentos de faturamento.", "BILLING", "billing_recent")
        if any(x in q for x in ("divergência", "divergencia", "erro", "diferença", "diferenca")):
            return AiDecision("Vou procurar divergências nos valores registrados.", "RECONCILE", "billing_divergences")
        if any(x in q for x in ("apagar", "excluir", "deletar", "remover")):
            return AiDecision("Essa ação altera dados e precisa de confirmação explícita.", "MUTATION", None, {}, True)
        return AiDecision("Posso analisar o resumo, consultar faturamento e procurar divergências. Conecte um provedor LLM depois para linguagem livre.", "GENERAL")
