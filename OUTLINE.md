# Roga — Project Outline

## One-liner

`roga` is a small Python command-line search tool for quick terminal questions: one query in, one concise web-grounded answer with readable examples out.

```bash
roga "python: methods to join lists"
```

## What It Is

Roga covers the kinds of questions that interrupt work in a terminal:

- Linux commands and common system administration tasks
- shell syntax, flags, redirection, and pipelines
- Python and other programming-language lookups
- short explanations of errors and technical concepts
- quick “how do I do this?” questions

It is not a research agent. Deeper comparisons, multi-step investigation, news research, and exploratory browsing remain browser work.

## Intended Output

Every answer should favour the same simple structure:

1. A brief explanation that directly answers the query.
2. A few common methods or examples, grouped only when useful.
3. Small fenced code blocks with language labels.
4. A short recommendation or important warning when one genuinely helps.
5. Compact Markdown source links supplied by the web-grounded response.

The output is rendered as Markdown through Rich so headings, lists, links, and code blocks look clean in Ghostty.

## Why It Exists

Roga solves a real daily problem while staying close enough to the developer's current Python ability to be built and understood without an agent writing most of it.

The learning objective is not agent architecture. It is to practise a short chain of ordinary, employable Python skills:

- accepting command-line arguments;
- loading a secret from the environment;
- calling an external API;
- separating request logic from terminal presentation;
- handling expected failures cleanly;
- testing without spending API credits;
- packaging a Python project as a real shell command.

The finished tool matters more than architectural fireworks. Every shipping line should be explainable by its author.

## Architecture

Roga uses a fixed pipeline:

```text
command-line query
    → one OpenRouter Chat Completions request with the web plugin
    → Markdown answer with citations
    → Rich rendering in Ghostty
```

There is no agent loop. The model cannot decide to call tools repeatedly. OpenRouter performs one web search for the request and grounds the model's answer with those results.

## Stack

- **Language:** Python 3.12+
- **Project workflow:** `uv`, src layout
- **CLI parser:** `argparse` from the standard library
- **LLM client:** OpenAI Python SDK pointed at OpenRouter
- **Search:** OpenRouter `web` plugin, initially using Exa with three results
- **Terminal rendering:** Rich Markdown
- **Environment loading:** python-dotenv
- **Testing:** pytest with a fake OpenAI client; no live calls in tests
- **Secrets:** `OPENROUTER_API_KEY` in `.env` or the shell environment
- **Model selection:** `ROGA_MODEL`, defaulting initially to the familiar `google/gemini-2.5-flash`

## V1 Scope

- Console command: `roga "question"`
- Exactly one required positional query
- Exactly one OpenRouter request per invocation
- Live web grounding on every request
- A focused system prompt that produces brief explanations and practical code examples
- Buffered output: wait for the complete answer, then render it correctly
- Rich Markdown rendering in an interactive terminal
- Clean errors for missing keys, authentication, rate limits, connection problems, and empty responses
- Unit tests using a fake client
- Installation with `uv tool install .`
- README with setup, usage, examples, and troubleshooting

## Explicitly Not in V1

- Agent loops or model-selected tools
- Firecrawl SDK or a second search account
- Streaming output
- Piped stdin or log analysis
- Interactive chat or follow-up questions
- Multiple commands or subcommands
- Flags for models, search engines, output styles, or result counts
- Caching, history, configuration files, databases, or telemetry
- Automatic query classification
- Raw citation-annotation parsing or source reconstruction
- A TUI, browser automation, or deep-research mode
- A `SKILL.md`

These can be considered only after V1 is finished, understood, and used. “Might be handy later” is not a requirement; it is scope creep in a novelty moustache.

## Project Shape

The application should stay small:

- `main.py` owns CLI input, environment loading, error presentation, and Rich output.
- `search.py` owns construction and execution of the one OpenRouter request.
- `prompts.py` owns the answer-format instruction.
- Two focused test files cover request behaviour and CLI behaviour.

## Success Criteria

Roga is complete when:

- `roga "python: methods to join lists"` produces a short explanation followed by useful fenced Python examples.
- `roga "linux: find files larger than 1GB"` produces an appropriate command, explains it briefly, and includes any important caution.
- Answers are based on live web results and contain source links.
- Output is clean and readable in Ghostty.
- Expected failures produce one actionable terminal message rather than a traceback.
- The test suite passes without an API key, network access, or API charges.
- `uv tool install .` exposes `roga` outside the repository.
- The developer can explain the purpose and flow of every source file and public function.

## Definition of “Simple”

Simple does not mean careless or fake. It means:

- one external service;
- one API request;
- one output path;
- standard-library CLI parsing;
- no abstraction without a present need;
- no feature added merely to impress a hypothetical hiring manager.
