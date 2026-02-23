"""
schemas.py - Pydantic Schemas (Data Validation)
-------------------------------------------------
Schemas define WHAT DATA the API accepts and returns.
They are NOT database models — they are validation rules.

- StudentCreate: Validates data when ADDING a new student
- StudentResponse: Shapes the data when RETURNING student info

Why separate from models.py?
→ Models define the DATABASE structure
→ Schemas define the API REQUEST/RESPONSE structure
"""

from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class StudentCreate(BaseModel):
    """
    Schema for creating a new student.
    The API will reject requests that don't match these rules.
    """
    name: str = Field(..., min_length=1, max_length=100, examples=["Rahul Kumar"])
    email: str = Field(..., min_length=5, max_length=100, examples=["rahul@example.com"])
    age: int = Field(..., ge=16, le=100, examples=[21])


class StudentResponse(BaseModel):
    """
    Schema for returning student data in API responses.
    This controls what the client sees.
    """
    id: int
    name: str
    email: str
    age: int
    created_at: datetime

    # This tells Pydantic to read data from SQLAlchemy model objects
    model_config = {"from_attributes": True}
