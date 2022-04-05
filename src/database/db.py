import os
from click import echo
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from dotenv import dotenv_values
config = dotenv_values('.env')
SQLALCHEMY_DATABASE_URL = config['DATABASE_UR']
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, future=True, echo=True)

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
