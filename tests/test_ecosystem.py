from core.config import DEFAULT_API_URL
from core.models import AppEntitlement, AppDefinition, Organization


def test_ecosystem_models_parse():
    org = Organization.from_dict({"id": "1", "name": "Example", "type": "SERVICES"})
    entitlement = AppEntitlement.from_dict({"appId": "instrua", "plan": "PREMIUM"})
    app = AppDefinition.from_dict(
        {
            "id": "instrua",
            "name": "Instrua",
            "description": "Atendimento",
            "installed": True,
        }
    )

    assert org.id == "1"
    assert org.organization_type == "SERVICES"
    assert entitlement.plan == "PREMIUM"
    assert app.installed is True


def test_default_api_url_is_local():
    assert DEFAULT_API_URL.startswith("http://127.0.0.1:")
