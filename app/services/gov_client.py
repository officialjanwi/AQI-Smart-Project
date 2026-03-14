from __future__ import annotations
import requests
from app.core.config import settings

def fetch_gov_aqi() -> dict:
    # If no URL set, return mock data
    if not settings.GOV_AQI_API_URL:
        return {"source": "mock", "aqi": 160, "status": "ok"}

    headers = {}
    if settings.GOV_AQI_API_KEY:
        # Many APIs accept Bearer tokens; adjust later if your API uses a different scheme
        headers["Authorization"] = f"Bearer {settings.GOV_AQI_API_KEY}"

    r = requests.get(settings.GOV_AQI_API_URL, headers=headers, timeout=10)
    r.raise_for_status()
    return {"source": "gov", "data": r.json(), "status": "ok"}
