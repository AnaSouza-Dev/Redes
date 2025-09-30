"""Application configuration settings."""

from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuração Runtime obtida via variáveis de ambiente"""

    server_ip: str = "auto"
    iface: str = "any"
    window_seconds: int = 5
    retention_seconds: int = 300

    model_config = SettingsConfigDict(env_file=".env", env_prefix="", env_nested_delimiter="__")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Se server_ip for "auto", usar 0.0.0.0 para capturar todo tráfego
        if self.server_ip == "auto":
            self.server_ip = "0.0.0.0"
        # Log para debug
        print(f"DEBUG: Final SERVER_IP = {self.server_ip}")


@lru_cache
def get_settings() -> Settings:
    """Retornar uma instância de configurações em cache"""

    return Settings()


