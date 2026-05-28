"""
FastMCP Echo Server
"""

import sys
from pathlib import Path

SRC = (Path(__file__).resolve().parent / "src").as_posix()
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from server.app import mcp  # noqa: E402,F401
