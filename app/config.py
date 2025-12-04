from pydantic_settings import BaseSettings, SettingsConfigDict


class _Settings(BaseSettings):
    DB_URL: str
    JWT_ACCESS_SECRET_KEY: str
    JWT_ACCESS_EXP: dict[str, int] = {"minutes": 30}

    SHORT_CODE_LEN: int = 8

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)


settings = _Settings()
