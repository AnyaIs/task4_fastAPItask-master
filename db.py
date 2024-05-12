from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import DB_PORT, DB_HOST, DB_NAME,DB_PASS,DB_USER
from models import Base

DATABASE_URL=f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine=create_engine(DATABASE_URL, echo=True)
Session=sessionmaker()

async def init_db():
    Base.metadata.create_all(bind=engine)
