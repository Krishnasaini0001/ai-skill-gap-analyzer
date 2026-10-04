from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    database_url: str
    secret_key: str
    access_token_expire_minutes: int = 60
    llm_api_key: str = ""
    llm_model: str = ""
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"


settings = Settings()