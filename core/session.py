from __future__ import annotations


class Session:
    def __init__(self) -> None:
        self.user_id: str | None = None
        self.name: str | None = None
        self.email: str | None = None
        self.roles: set[str] = set()
        self.company_id: str | None = None

    @property
    def authenticated(self) -> bool:
        return bool(self.user_id)

    def clear(self) -> None:
        self.user_id = None
        self.name = None
        self.email = None
        self.roles.clear()
        self.company_id = None

    def apply_auth_response(self, data: dict) -> None:
        self.user_id = str(data["userId"])
        self.name = data.get("name")
        self.email = data.get("email")
        self.roles = set(data.get("roles") or [])
