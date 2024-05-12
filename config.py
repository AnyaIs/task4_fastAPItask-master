from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings


# class Settings(BaseSettings):
#     app_name: str
#     DB_HOST:str
#     DB_PORT:int
#     DB_NAME:str
#     DB_USER:str
#     DB_PASS:str



load_dotenv()

DB_HOST=os.environ.get("DB_HOST")
DB_PORT=int(os.environ.get("DB_PORT"))
DB_NAME=os.environ.get("DB_NAME")
DB_USER=os.environ.get("DB_USER")
DB_PASS=os.environ.get("DB_PASS")
