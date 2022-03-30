import os
import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values
config = dotenv_values('.env')
#SQLALCHEMY_DATABASE_URL = config['DATABASE_UR']
engine = create_async_engine("postgresql+asyncpg://postgres:admin@localhost/postgres", future=True, echo=True)
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
Async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession )
Base = declarative_base()


def get_db():
    try:
        db = Async_session()
        return  db
    finally:
        db.close()