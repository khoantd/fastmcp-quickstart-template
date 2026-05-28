from fastmcp import FastMCP


def register(mcp: FastMCP) -> None:
    @mcp.resource("echo://static")
    def echo_resource() -> str:
        return "Echo!"

    @mcp.resource("echo://{text}")
    def echo_template(text: str) -> str:
        """Echo the input text"""

        return f"Echo: {text}"

