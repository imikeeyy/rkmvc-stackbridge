"""
config.py - Application Configuration
--------------------------------------
Loads environment variables from the .env file.
We keep all configuration in one place for easy management.
"""

import os
from dotenv import load_dotenv

# Load variables from .env file into the environment
load_dotenv()

# Database connection URL (read from .env file)
# Example: postgresql+asyncpg://postgres:postgres@localhost:5432/stackbridge
DATABASE_URL: str = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://postgres:postgres@localhost:5432/stackbridge"
)
