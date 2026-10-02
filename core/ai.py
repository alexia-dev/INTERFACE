from __future__ import annotations

from core.ai_provider import AiProvider, AiRequest, AiDecision, MockAiProvider
from core.ai_tools import AiTools


class NexaAi:
    TOOLS=("summary","billing_recent","billing_divergences")

    def __init__(self, database, provider: AiProvider | None = None):
        self.tools=AiTools(database)
        self.provider=provider or MockAiProvider()

    def ask(self, message: str) -> dict:
        decision: AiDecision=self.provider.decide(AiRequest(message, {"product":"NEXA"}, self.TOOLS))
        data={}
        if decision.tool:
            data=getattr(self.tools, decision.tool)()
        return {"message":decision.text,"intent":decision.intent,"tool":decision.tool,"data":data,"requires_confirmation":decision.requires_confirmation}
