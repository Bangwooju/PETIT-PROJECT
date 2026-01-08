from pydantic_settings import BaseSettings
from pathlib import Path
from dotenv import load_dotenv
import os

# .env 파일 로드
BASE_DIR = Path(__file__).resolve().parents[2]
dotenv_path = BASE_DIR / ".env"

load_dotenv(dotenv_path)

class Settings(BaseSettings):
    # DB 설정
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    # Google Cloud 서비스 계정 파일 경로
    GEMINI_API_KEY: str


    class Config:
        env_file = dotenv_path

settings = Settings()