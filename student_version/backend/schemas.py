"""
schemas.py - Pydantic Schemas (Data Validation)
-------------------------------------------------
Schemas define WHAT DATA the API accepts and returns.

# TODO: STUDENT TASK — Complete the StudentCreate schema
"""

from datetime import datetime
from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    """
    Schema for creating a new student.

    # TODO: STUDENT TASK
    # Add three fields with validation:
    # 1. name: str (min_length=1, max_length=100)
    # 2. email: str (min_length=5, max_length=100)
    # 3. age: int (ge=16, le=100)
    #
    # Example:
    #   name: str = Field(..., min_length=1, max_length=100)
    """
    pass  # Remove this line and add fields above


class StudentResponse(BaseModel):
    """
    Schema for returning student data in API responses.
    ✅ This schema is COMPLETE.
    """
    id: int
    name: str
    email: str
    age: int
    created_at: datetime

    model_config = {"from_attributes": True}
