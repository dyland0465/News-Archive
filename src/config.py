import os
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / '.env'
load_dotenv(dotenv_path=env_path)


# API config
API_KEY = os.getenv("NEWS_API_KEY")
COUNTRY = os.getenv("COUNTRY", "us")


if not API_KEY:
    raise ValueError("ERROR: API Key missing from .env file")

    DB_CONFIG = {
        "host": os.getenv("DB_HOST", "localhost"),
        "user": os.getenv("DB_USER", "news_pipeline_user"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_NAME", "news_db")
    }

    if not DB_CONFIG["password"]:
        raise ValueError("ERROR: Password missing from .env file")
