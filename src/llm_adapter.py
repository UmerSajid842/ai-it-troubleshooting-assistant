"""Optional adapter boundary for an OpenAI-compatible chat endpoint."""
import json
import os
from typing import Any

import requests


def generate_structured_reply(user_text: str) -> dict[str, Any]:
    """Call a configured endpoint; fail closed when configuration is absent."""
    endpoint = os.getenv("LLM_BASE_URL")
    api_key = os.getenv("LLM_API_KEY")
    model = os.getenv("LLM_MODEL", "local-model")
    if not endpoint or not api_key:
        raise RuntimeError("LLM endpoint is not configured; use the deterministic assistant path.")
    response = requests.post(
        endpoint.rstrip("/") + "/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={"model": model, "messages": [{"role": "user", "content": user_text}], "temperature": 0},
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    content = payload["choices"][0]["message"]["content"]
    parsed = json.loads(content)
    if not isinstance(parsed, dict) or "steps" not in parsed:
        raise ValueError("LLM response did not match the expected structured shape.")
    return parsed
