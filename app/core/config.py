from pydantic_settings import BaseSettings
from pathlib import Path
from fastapi.staticfiles import StaticFiles

# Path to the .env file in root directory
ENV_PATH = Path(__file__).resolve().parent.parent.parent / ".env"

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str

    class Config:
        env_file = ENV_PATH
        env_file_encoding = 'utf-8'

settings = Settings()


STATIC_DIR = Path(__file__).resolve().parent.parent.parent / "static"

def mount_static(app):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")