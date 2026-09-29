from __future__ import annotations

import os
import sys

DEFAULT_API_URL = "http://127.0.0.1:8080"


def api_base_url() -> str:
    """Resolve the API URL for local development and packaged builds."""
    configured = os.getenv("NEXA_API_URL")
    if configured:
        return configured.rstrip("/")

    if sys.platform == "android":
        return "http://10.0.2.2:8080"

    return DEFAULT_API_URL
