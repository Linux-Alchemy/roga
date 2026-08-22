# temp placeholder for file description

from typing import Any
from roga_cli.prompts import build_messages

DEFAULT_MODEL: str = "google/gemini-2.5-flash"


def build_request(query: str, model: str) -> dict[str, Any]:
    """Build keywork args for one web-grounded chat completion.

    Args:
        query: the user's validated search question.
        model: the OpenRouter model used for the search

    Returns:
        JSON compatible request args containing the model, message,
        and one OpenRouter web plugin configured for 3 results.

    Raises:
    ValueError: if the query or model arg is empty
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

