from server.app import create_app


def test_create_app_smoke() -> None:
    mcp = create_app()
    assert mcp is not None


def test_echo_tool_roundtrip() -> None:
    from server.tools.echo import echo

    assert echo("hello") == "hello"

