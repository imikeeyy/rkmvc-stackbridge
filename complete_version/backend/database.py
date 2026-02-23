"""
database.py - Database Connection Setup
----------------------------------------
Sets up the async SQLAlchemy engine and session.
Provides a dependency function (get_db) for FastAPI routes.

Key concepts:
- Engine: The connection to the database
- Session: A "conversation" with the database (open → query → close)
- Dependency Injection: FastAPI automatically provides a DB session to routes
"""

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from config import DATABASE_URL

# --- 1. Create the async database engine ---
# The engine manages the connection pool to PostgreSQL
engine = create_async_engine(DATABASE_URL, echo=True)

# --- 2. Create a session factory ---
# Each request gets its own session (like opening a new tab to the DB)
async_session = async_sessionmaker(engine, expire_on_commit=False)


# --- 3. Base class for all our database models ---
# Every table in our database will inherit from this class
class Base(DeclarativeBase):
    pass


# --- 4. Dependency function for FastAPI ---
# This function is called automatically by FastAPI for each request.
# It opens a session, gives it to the route, then closes it.
async def get_db():
    """Provide a database session to each API request."""
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()
