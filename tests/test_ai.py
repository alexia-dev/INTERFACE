from core.ai import NexaAi
from core.ai_provider import MockAiProvider
from core.database import Database


def test_ai_summary(tmp_path):
    db=Database(tmp_path / "nexa.db")
    db.initialize()
    result=NexaAi(db, MockAiProvider()).ask("me dê um resumo")
    assert result["tool"] == "summary"
    assert "billing" in result["data"]


def test_ai_requires_confirmation():
    db=Database(":memory:")
    db.initialize()
    result=NexaAi(db).ask("apague tudo")
    assert result["requires_confirmation"] is True
