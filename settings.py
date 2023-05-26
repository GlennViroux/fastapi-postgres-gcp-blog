from pathlib import Path

from pydantic import BaseSettings

class Settings(BaseSettings):
    DB_NAME: str
    DB_HOST: str
    DB_USER: str
    DB_PASS: str

settings = Settings(_env_file=Path(__file__).parent/ ".env", _env_file_encoding="utf-8")

