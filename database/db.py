from fastapi import HTTPException
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from dotenv import dotenv_values
config = dotenv_values('.env')
#SQLALCHEMY_DATABASE_URL = config['DATABASE_UR']
#engine = create_async_engine("postgresql+asyncpg://postgres:admin@localhost/postgres", future=True, echo=True)
engine = create_async_engine("postgresql+asyncpg://hqlbqoamjvzggz:1ca892eeeb649dcd089eb18f2dd5c156f189da45232de14556cc4730f6f6a907@ec2-52-200-215-149.compute-1.amazonaws.com:5432/d8tft2pm3p4ua0", future=True, echo=True)
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
Base = declarative_base()



async def get_db() -> AsyncGenerator:
    asyncsession = sessionmaker(
        expire_on_commit=False,
         class_=AsyncSession,
          bind=engine
    )
    async with asyncsession() as session:
        try:
            yield session
            await session.commit()
        except SQLAlchemyError as sql_ex:
            await session.rollback()
            raise sql_ex
        except HTTPException as http_ex:
            await session.rollback()
            raise http_ex
        finally:
            await session.close()