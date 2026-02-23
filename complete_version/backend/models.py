"""
models.py - Database Models (SQLAlchemy)
-----------------------------------------
Defines the structure of our database tables.
Each class here maps to one table in PostgreSQL.

Think of a Model as a blueprint for a table:
- Class name  → Table name
- Attributes  → Columns
"""

from datetime import datetime
from sqlalchemy import String, Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Student(Base):
    """
    Student table - stores student information.

    Columns:
    - id:         Auto-generated unique identifier
    - name:       Student's full name
    - email:      Student's email (must be unique)
    - age:        Student's age
    - created_at: Timestamp when the record was created
    """

    # This tells SQLAlchemy the table name in PostgreSQL
    __tablename__ = "students"

    # --- Column Definitions ---
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
