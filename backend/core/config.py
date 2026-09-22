from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator

class Settings(BaseSettings):
    DATABASE_URL: str
    API_PREFIX: str = "/api"
    DEBUG: bool = False
    ALLOWED_ORIGINS: List[str] = []
    AI_API_KEY: str = ""

    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(cls, v) -> List[str]:
        return v.split(",") if v else []

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_sensitive = True

settings = Settings()