from __future__ import annotations

import os


DEFAULT_API_URL = "http://127.0.0.1:8080"


def api_base_url() -> str:
    """Return the configured NEXA API URL."""
    return os.getenv("NEXA_API_URL", DEFAULT_API_URL).rstrip("/")
