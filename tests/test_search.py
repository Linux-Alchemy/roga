# temp placeholder for file description

from roga_cli.prompts import SYSTEM_PROMPT, build_messages
import pytest

def test_build_messages_returns_messages_in_order() -> None:
    test_query: str = "python: how to join lists"
    messages =  build_messages(test_query)
    assert len(messages) == 2
    assert messages[0]['role'] == 'system'
    assert messages[0]['content'] == SYSTEM_PROMPT
    assert messages[1]['role'] == 'user'
    assert messages[1]['content'] == test_query


def test_build_message_preserves_query() -> None:
    test_query: str = " test query with white space "
    messages = build_messages(test_query)
    assert messages[1]['content'] == test_query


def test_build_messages_rejects_empty_query() -> None:
    with pytest.raises(ValueError, match="Query cannot be empty"):
        build_messages("")

    with pytest.raises(ValueError, match="Query cannot be empty"):
        build_messages(" ")



