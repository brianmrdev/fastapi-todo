import os

from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):

    db_name: str = os.getenv('POSTGRES_DB')
    db_user: str = os.getenv('POSTGRES_USER')
    db_pass: str = os.getenv('POSTGRES_PASSWORD')
    db_host: str = os.getenv('DB_HOST')
    db_port: str = os.getenv('DB_PORT')
    
    secret_key: str = os.getenv('SECRET_KEY')
    token_expire: int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')