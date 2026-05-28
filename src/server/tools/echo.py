from fastmcp import FastMCP


def echo(text: str) -> str:
    return text


def register(mcp: FastMCP) -> None:
    @mcp.tool
    def echo_tool(text: str) -> str:
        """Echo the input text"""

        return echo(text)

