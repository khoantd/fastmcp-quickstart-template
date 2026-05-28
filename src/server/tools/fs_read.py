from __future__ import annotations

from pathlib import Path

from fastmcp import FastMCP

from server.settings import settings


def _resolve_safe_path(relative_path: str) -> Path:
    base = settings.safe_base_dir.resolve()
    candidate = (base / relative_path).resolve()
    if base == candidate or base in candidate.parents:
        return candidate
    raise ValueError("Path escapes SAFE_BASE_DIR")


def read_text_file(relative_path: str) -> str:
    path = _resolve_safe_path(relative_path)
    return path.read_text(encoding="utf-8")


def register(mcp: FastMCP) -> None:
    @mcp.tool
    def read_file_tool(path: str) -> str:
        """Read a UTF-8 text file within SAFE_BASE_DIR."""

        return read_text_file(path)

