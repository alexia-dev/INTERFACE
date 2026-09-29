from core.api_client import ApiClient, ApiError
from core.session import Session


def test_session_starts_unauthenticated():
    session = Session()
    assert not session.authenticated
    assert session.roles == set()


def test_session_applies_auth_response():
    session = Session()
    session.apply_auth_response(
        {
            "userId": "123",
            "name": "Teste",
            "email": "teste@example.com",
            "roles": ["COMPANY_ADMIN", "RECEPTION"],
        }
    )
    assert session.authenticated
    assert session.user_id == "123"
    assert session.name == "Teste"
    assert session.roles == {"COMPANY_ADMIN", "RECEPTION"}


def test_api_error_keeps_status():
    error = ApiError(401, "não autorizado")
    assert error.status_code == 401
    assert error.message == "não autorizado"


def test_api_client_strips_base_url_slash():
    client = ApiClient("http://localhost:8080/")
    assert client.base_url == "http://localhost:8080"
