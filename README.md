# FastMCP agent-ready template (Cloud-first)

This template is a **FastMCP server** that’s structured for **agent-driven iteration**:
- A real `src/` package layout (easy to extend safely)
- Fast local dev with **uv**
- Quality gates (lint/typecheck/tests)
- Clear extension points for tools/resources/prompts

## What’s included
- **Entry point**: `echo.py` (kept stable for compatibility; imports the packaged app)
- **Server package**: `src/server/app.py` exports `mcp`
- **Echo examples**:
  - Tool: `src/server/tools/echo.py`
  - Resources: `src/server/resources/echo.py`
  - Prompt: `src/server/prompts/echo.py`
- **More examples**:
  - Validated tool input (pydantic): `src/server/tools/validated.py`
  - Filesystem-safe tool: `src/server/tools/fs_read.py`
  - HTTP client tool (allowlist + timeout): `src/server/tools/http_fetch.py`

## Deploy (FastMCP Cloud)
- Create a [FastMCP Cloud account](http://fastmcp.cloud/signup)
- Connect GitHub
- Select **Clone our template** and deploy

FastMCP Cloud should start the server using the repository entrypoint. This template keeps `echo.py` as the canonical entrypoint so both Cloud and local runs behave the same.

## Local development (uv)
Prereqs: install `uv`.

- Install deps:

```bash
uv sync
```

- Run the server entrypoint:

```bash
uv run python echo.py
```

## Common commands
If you prefer make targets:

```bash
make sync
make dev
make lint
make format
make typecheck
make test
```

## Safely adding new capabilities (agent-friendly)
- **Add a tool**: create a module in `src/server/tools/` and register it from `src/server/app.py`
- **Add a resource**: create a module in `src/server/resources/` and register it from `src/server/app.py`
- **Add a prompt**: create a module in `src/server/prompts/` and register it from `src/server/app.py`

See `AGENTS.md` for invariants and patterns that help avoid breaking working behavior.

## Learn more
- [FastMCP Documentation](https://gofastmcp.com/)
- [MCP Protocol](https://modelcontextprotocol.io/)
