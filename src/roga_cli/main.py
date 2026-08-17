# temp placeholder for file description
from argparse import ArgumentParser
from rich import markdown
from rich.console import Console
from rich.markdown import Markdown


def parse_query() -> str:
    """Parse and return the CLI query.

    Returns:
        Non-empty query supplied to the 'roga' command.

    Raise:
        SystemExit: if query is absent or invalid.
    """

    parser: ArgumentParser = ArgumentParser(description="Roga Terminal Search Tool")
    parser.add_argument("query", type=str, help="User prompt")
    args = parser.parse_args()
    return args.query


def render_answer(answer: str) -> None:
    """Render the answer in markdown to the terminal.

    Args:
        answer: Non-empty markdown text

    Raises:
        ValueError: if answer is empty or only white space.
    """
    console: Console = Console()
    if not answer.strip():
        raise ValueError("Answer cannot be empty or whitespace-only")

    markdown_object = Markdown(answer)
    console.print(markdown_object)



def main() -> None:
    """Runs one 'roga' query and renders the answer.

    Raises:
        SystemExit: if command input is invalid.
    """
    parse_query()
    sample_answer: str = """# Joining Python Lists

    Use the `+` operator to combine two lists:

    ```python
    first = [1, 2]
    second = [3, 4]
    combined = first + second
    '''
    """
    render_answer(sample_answer)

