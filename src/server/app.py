from fastmcp import FastMCP


def create_app() -> FastMCP:
    from server.settings import settings

    mcp = FastMCP(settings.server_name)

    # Tools
    from server.tools.echo import register as register_echo_tool

    register_echo_tool(mcp)

    from server.tools.fs_read import register as register_fs_read_tool

    register_fs_read_tool(mcp)

    from server.tools.http_fetch import register as register_http_fetch_tool

    register_http_fetch_tool(mcp)

    from server.tools.validated import register as register_validated_tool

    register_validated_tool(mcp)

    # Resources
    from server.resources.echo import register as register_echo_resources

    register_echo_resources(mcp)

    # Prompts
    from server.prompts.echo import register as register_echo_prompts

    register_echo_prompts(mcp)

    return mcp


mcp = create_app()

