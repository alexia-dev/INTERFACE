from core.ai_http_provider import OpenAiCompatibleProvider
from core.ai_provider import MockAiProvider


class AiProviderRouter:
    def __init__(self):
        self.external=OpenAiCompatibleProvider()
        self.mock=MockAiProvider()

    def decide(self, request):
        if self.external.configured():
            try:
                return self.external.decide(request)
            except Exception:
                pass
        return self.mock.decide(request)
