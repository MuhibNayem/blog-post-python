import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Blog"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:password@db:5432/blog_post")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "4eb17128-c0c4-4f85-adc3-36dc56fa3aaa")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 120

settings = Settings()
