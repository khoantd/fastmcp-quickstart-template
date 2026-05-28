from __future__ import annotations

import re

from fastmcp import FastMCP
from pydantic import BaseModel, Field


class WordCountRequest(BaseModel):
    text: str = Field(min_length=1, max_length=50_000)
    lowercase: bool = True


def word_count(req: WordCountRequest) -> dict[str, int]:
    text = req.text.lower() if req.lowercase else req.text
    words = re.findall(r"[A-Za-z0-9']+", text)
    unique = {w for w in words if w}
    return {"words": len(words), "unique_words": len(unique)}


def register(mcp: FastMCP) -> None:
    @mcp.tool
    def word_count_tool(req: WordCountRequest) -> dict[str, int]:
        """Count words with validated inputs (pydantic model)."""

        return word_count(req)

