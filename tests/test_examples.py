import pytest

from server.tools.fs_read import _resolve_safe_path
from server.tools.validated import WordCountRequest, word_count


def test_word_count_validated() -> None:
    out = word_count(WordCountRequest(text="Hello hello world"))
    assert out["words"] == 3
    assert out["unique_words"] == 2


def test_resolve_safe_path_blocks_escape(tmp_path) -> None:
    # point SAFE_BASE_DIR at tmp_path by temporarily mutating settings
    from server import settings as settings_module

    old = settings_module.settings.safe_base_dir
    try:
        settings_module.settings.safe_base_dir = tmp_path
        _resolve_safe_path("a.txt")
        with pytest.raises(ValueError):
            _resolve_safe_path("../escape.txt")
    finally:
        settings_module.settings.safe_base_dir = old

