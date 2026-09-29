from __future__ import annotations

from typing import Any

import requests


class ApiError(RuntimeError):
    def __init__(self, status_code: int, message: str):
        super().__init__(message)
        self.status_code = status_code
        self.message = message


class ApiClient:
    """Small REST client shared by desktop and Android builds."""

    def __init__(self, base_url: str = "http://127.0.0.1:8080"):
        self.base_url = base_url.rstrip("/")
        self.access_token: str | None = None
        self.company_id: str | None = None

    def configure(self, base_url: str | None = None) -> None:
        if base_url:
            self.base_url = base_url.rstrip("/")

    def clear_session(self) -> None:
        self.access_token = None
        self.company_id = None

    def _request(self, method: str, path: str, **kwargs: Any) -> Any:
        headers = kwargs.pop("headers", {})
        if self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"

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
        payload = {"email": email, "password": password}
        data = self._request("POST", "/api/v1/auth/login", json=payload)
        self.access_token = data["accessToken"]
        return data

    def list_companies(self) -> list[dict[str, Any]]:
        return self._request("GET", "/api/v1/companies")

    def list_patients(self, company_id: str) -> list[dict[str, Any]]:
        return self._request("GET", f"/api/v1/companies/{company_id}/patients")
