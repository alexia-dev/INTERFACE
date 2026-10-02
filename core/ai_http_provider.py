from __future__ import annotations

import json
import os
from urllib.request import Request, urlopen
from core.ai_provider import AiDecision, AiRequest


class OpenAiCompatibleProvider:
    def __init__(self):
        self.api_key=os.getenv("NEXA_AI_API_KEY","")
        self.base_url=os.getenv("NEXA_AI_BASE_URL","https://api.openai.com/v1/responses")
        self.model=os.getenv("NEXA_AI_MODEL","gpt-6-luna")

    def configured(self) -> bool:
        return bool(self.api_key.strip())

    def decide(self, request: AiRequest) -> AiDecision:
        if not self.configured():
            raise RuntimeError("NEXA_AI_API_KEY não configurada")
        system=("Você é o NEXA AI. Responda SOMENTE JSON válido com as chaves "
                "text,intent,tool,arguments,requires_confirmation. "
                f"Ferramentas autorizadas: {list(request.allowed_tools)}. "
                "Nunca invente dados. Use tool null quando nenhuma ferramenta for adequada. "
                "Ações mutáveis devem exigir confirmação.")
        payload={"model":self.model,"instructions":system,"input":request.message}
        req=Request(self.base_url,data=json.dumps(payload).encode(),headers={"Authorization":f"Bearer {self.api_key}","Content-Type":"application/json"},method="POST")
        with urlopen(req,timeout=30) as response:
            body=json.loads(response.read().decode())
        content=body["output"][0]["content"][0]["text"]
        parsed=json.loads(content)
        tool=parsed.get("tool")
        if tool not in request.allowed_tools:
            tool=None
        return AiDecision(str(parsed.get("text","")),str(parsed.get("intent","GENERAL")),tool,parsed.get("arguments") or {},bool(parsed.get("requires_confirmation",False)))
