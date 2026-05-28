from __future__ import annotations

import httpx
from fastmcp import FastMCP

from server.settings import settings


def _is_allowlisted(url: str) -> bool:
    prefixes = settings.allowlisted_prefixes()
    if not prefixes:
        return False
    return any(url.startswith(p) for p in prefixes)


async def fetch_text(url: str) -> str:
    if not _is_allowlisted(url):
        raise ValueError("URL not allowlisted by HTTP_ALLOWLIST")

    timeout = httpx.Timeout(10.0, connect=5.0)
    async with httpx.AsyncClient(timeout=timeout, follow_redirects=True) as client:
        resp = await client.get(
            url,
            headers={"User-Agent": "fastmcp-quickstart-template/0.1"},
        )
        resp.raise_for_status()
        return resp.text


def register(mcp: FastMCP) -> None:
    @mcp.tool
    async def fetch_url_tool(url: str) -> str:
        """Fetch a URL (must match HTTP_ALLOWLIST prefixes)."""

        return await fetch_text(url)

