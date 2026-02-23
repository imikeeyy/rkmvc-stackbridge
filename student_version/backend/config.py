"""
config.py - Application Configuration
--------------------------------------
Loads environment variables from the .env file.
"""

import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL: str = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://postgres:postgres@localhost:5432/stackbridge"
)
