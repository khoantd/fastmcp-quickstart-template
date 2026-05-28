from fastmcp import FastMCP


def register(mcp: FastMCP) -> None:
    @mcp.prompt("echo")
    def echo_prompt(text: str) -> str:
        return text

