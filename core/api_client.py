from __future__ import annotations

from typing import Any

import requests

from core.config import api_base_url


class ApiError(RuntimeError):
    def __init__(self, status_code: int, message: str):
        super().__init__(message)
        self.status_code = status_code
        self.message = message


class ApiClient:
    """REST client for shared NEXA services and product APIs."""

    def __init__(self, base_url: str | None = None):
        self.base_url = (base_url or api_base_url()).rstrip("/")
        self.access_token: str | None = None
        self.organization_id: str | None = None

    def configure(self, base_url: str | None = None) -> None:
        if base_url:
            self.base_url = base_url.rstrip("/")

    def set_context(self, *, organization_id: str | None = None) -> None:
        self.organization_id = organization_id

    def clear_session(self) -> None:
        self.access_token = None
        self.organization_id = None

    def _request(self, method: str, path: str, **kwargs: Any) -> Any:
        headers = dict(kwargs.pop("headers", {}))
        if self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"
        if self.organization_id:
            headers["X-NEXA-Organization"] = self.organization_id

        response = requests.request(
            method,
            f"{self.base_url}{path}",
            timeout=15,
            headers=headers,
            **kwargs,
        )

        if response.status_code >= 400:
            try:
                payload = response.json()
                message = payload.get("message") or payload.get("error") or response.text
            except ValueError:
                message = response.text or "Erro de comunicação com a API."
            raise ApiError(response.status_code, message)

        if not response.content:
            return None
        try:
            return response.json()
        except ValueError:
            return response.text

    def login(self, email: str, password: str) -> dict[str, Any]:
        data = self._request(
            "POST",
            "/api/v1/auth/login",
            json={"email": email, "password": password},
        )
        self.access_token = data["accessToken"]
        return data

    def list_companies(self) -> list[dict[str, Any]]:
        return self._request("GET", "/api/v1/companies")

    def list_apps(self) -> list[dict[str, Any]]:
        return self._request("GET", "/api/v1/apps")

    def get_me(self) -> dict[str, Any]:
        return self._request("GET", "/api/v1/me")

    def get_entitlements(self) -> list[dict[str, Any]]:
        return self._request("GET", "/api/v1/me/entitlements")

    def get_organizations(self) -> list[dict[str, Any]]:
        return self._request("GET", "/api/v1/me/organizations")

    def list_patients(self, company_id: str) -> list[dict[str, Any]]:
        return self._request("GET", f"/api/v1/companies/{company_id}/patients")

    def list_appointments(self, company_id: str) -> list[dict[str, Any]]:
        return self._request("GET", f"/api/v1/companies/{company_id}/appointments")

    def get_journey_summary(self, company_id: str) -> dict[str, Any]:
        return self._request("GET", f"/api/v1/companies/{company_id}/journey/summary")
