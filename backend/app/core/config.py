
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_TITLE: str = "Content Management System"
    PROJECT_VERSION: str = "0.0.1"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "cms_bd")

    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    ACCESS_TOKEN_EXPIRES_MINUTES = 30
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"


settings = Settings()