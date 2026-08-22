"""Build pure OpenRouter request arguments for Roga searches."""

from typing import Any
from roga_cli.prompts import build_messages

DEFAULT_MODEL: str = "google/gemini-2.5-flash"


def build_request(query: str, model: str) -> dict[str, Any]:
    """Build keyword arguments for one web-grounded chat completion.

    Args:
        query: The user's validated search question.
        model: The OpenRouter model used for the search.

    Returns:
        JSON-compatible request arguments containing the model, messages,
        and one OpenRouter web plugin configured for three results.

    Raises:
        ValueError: If the query or model is empty or whitespace-only.
    """

    if not model.strip():
        raise ValueError("Model name cannot be empty.")

    messages = build_messages(query)

    extra_body = {
        "plugins": [
            {
                "id": "web",
                "engine": "exa",
                "max_results": 3
            }
        ]
    }
    return {
        "model": model, 
        "messages": messages,
        "extra_body": extra_body
    }
