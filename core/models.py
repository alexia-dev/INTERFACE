from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class AppEntitlement:
    app_id: str
    plan: str = "FREE"
    features: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "AppEntitlement":
        return cls(
            app_id=str(payload.get("appId") or payload.get("app_id") or ""),
            plan=str(payload.get("plan") or "FREE"),
            features=dict(payload.get("features") or {}),
        )


@dataclass(slots=True)
class Organization:
    id: str
    name: str
    organization_type: str | None = None
    role: str | None = None

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "Organization":
        return cls(
            id=str(payload.get("id") or ""),
            name=str(payload.get("name") or ""),
            organization_type=payload.get("type") or payload.get("organizationType"),
            role=payload.get("role"),
        )


@dataclass(slots=True)
class AppDefinition:
    app_id: str
    name: str
    description: str
    installed: bool = False

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "AppDefinition":
        return cls(
            app_id=str(payload.get("id") or payload.get("appId") or ""),
            name=str(payload.get("name") or ""),
            description=str(payload.get("description") or ""),
            installed=bool(payload.get("installed", False)),
        )
