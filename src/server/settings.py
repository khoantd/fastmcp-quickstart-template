from __future__ import annotations

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    server_name: str = Field(default="Echo Server", alias="SERVER_NAME")
    safe_base_dir: Path = Field(default=Path("."), alias="SAFE_BASE_DIR")
    http_allowlist: str = Field(default="", alias="HTTP_ALLOWLIST")

    def allowlisted_prefixes(self) -> list[str]:
        return [p.strip() for p in self.http_allowlist.split(",") if p.strip()]


settings = Settings()

