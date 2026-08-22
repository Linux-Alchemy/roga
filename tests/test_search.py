"""Tests for Roga prompt and OpenRouter request construction."""

from roga_cli.prompts import SYSTEM_PROMPT, build_messages
from roga_cli.search import build_request
import pytest


# tests for prompts.py
def test_build_messages_returns_messages_in_order() -> None:
    """Return exactly one system message followed by the user message."""
    test_query: str = "python: how to join lists"
    messages =  build_messages(test_query)
    assert len(messages) == 2
    assert messages[0]['role'] == 'system'
    assert messages[0]['content'] == SYSTEM_PROMPT
    assert messages[1]['role'] == 'user'
    assert messages[1]['content'] == test_query


def test_build_message_preserves_query() -> None:
    """Preserve the user's query without trimming or rewriting it."""
    test_query: str = " test query with white space "
    messages = build_messages(test_query)
    assert messages[1]['content'] == test_query


def test_build_messages_rejects_empty_query() -> None:
    """Reject empty and whitespace-only user queries."""
    with pytest.raises(ValueError, match="Query cannot be empty"):
        build_messages("")

    with pytest.raises(ValueError, match="Query cannot be empty"):
        build_messages(" ")



# tests for search.py

def test_build_request_rejects_empty_model() -> None:
    """Reject empty and whitespace-only model identifiers."""
    test_query: str = "test query"
    with pytest.raises(ValueError, match="Model name cannot be empty"):
        build_request(query=test_query, model="")

    with pytest.raises(ValueError, match="Model name cannot be empty"):
        build_request(query=test_query, model=" ")


def test_build_request_has_only_one_plugin() -> None:
    """Configure exactly one OpenRouter plugin."""
    request = build_request(query="test query", model="test model")
    assert len(request["extra_body"]["plugins"]) == 1

def test_build_request_model() -> None:
    """Preserve the supplied model identifier in the request."""
    request = build_request(query="test query", model="test model")
    assert request["model"] == "test model"

def test_build_request_search_engine() -> None:
    """Configure Exa as the web-search engine."""
    request = build_request(query= "test query", model="test model")
    assert request["extra_body"]["plugins"][0]["engine"] == "exa"

def test_build_request_carries_query_from_build_messages() -> None:
    """Include the messages built from the supplied query."""
    request = build_request(query="test query", model="test model")
    assert request["messages"] == build_messages(query="test query")

def test_build_request_contains_plugin_id() -> None:
    """Identify the configured plugin as OpenRouter web search."""
    request = build_request(query="test query", model="test model")
    assert request["extra_body"]["plugins"][0]["id"]  == "web"

def test_build_request_contains_search_result_limit() -> None:
    """Limit web search to three results."""
    request = build_request(query= "test query", model="test model")
    assert request["extra_body"]["plugins"][0]["max_results"] == 3

def test_build_request_does_not_stream() -> None:
    """Leave streaming absent from the request arguments."""
    request = build_request(query="test query", model="test model")
    assert "stream" not in request
