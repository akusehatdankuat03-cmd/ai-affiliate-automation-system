from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "AI Affiliate Automation System"
    APP_ENV: str = "development"
    DEBUG: bool = True
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/affiliate_ai"
    REDIS_URL: str = "redis://localhost:6379/0"
    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""
    SHOPEE_API_KEY: str = ""
    SHOPEE_PARTNER_ID: str = ""
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
