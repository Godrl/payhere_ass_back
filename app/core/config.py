import pathlib
import os

from dotenv import load_dotenv
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, validator
from typing import List, Union
from pathlib import Path

base_path = Path()
basedir = str(base_path.cwd())
env_path = base_path.cwd() / f'app/core/settings/.env.{os.getenv("APP_ENV")}'

load_dotenv(env_path)

# Project Directories
ROOT = pathlib.Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    APP_ENV: str = 'dev'

    API_V1_STR: str = '/api/v1'
    JWT_SECRET: str = 'b8f55e34b60bfbeb8c00f709c8680fb38c958efca649bb63b709a54306317fe2'
    ALGORITHM: str = 'HS256'

    # 60 minutes * 24 hours * 1 days = 1 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 1

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        'http://localhost:8000',  # type: ignore
    ]

    @validator('BACKEND_CORS_ORIGINS', pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith('['):
            return [i.strip() for i in v.split(',')]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)


settings = Settings()
