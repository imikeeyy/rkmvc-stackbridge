"""
database.py - Database Connection Setup
----------------------------------------
✅ This file is COMPLETE. No changes needed.
"""

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from config import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def get_db():
    """Provide a database session to each API request."""
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()
