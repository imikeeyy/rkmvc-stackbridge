"""
routes.py - API Endpoints (Routes)
------------------------------------
Defines all the API endpoints for the Student resource.
Each function handles one HTTP request type.

REST API Pattern:
- GET    /students      → Get all students
- GET    /students/{id} → Get one student by ID
- POST   /students      → Add a new student
- DELETE /students/{id} → Delete a student by ID
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import get_db
from models import Student
from schemas import StudentCreate, StudentResponse

# Create a router — groups related endpoints together
router = APIRouter(prefix="/students", tags=["Students"])


# =============================================
# GET /students — Fetch all students
# =============================================
@router.get("/", response_model=list[StudentResponse])
async def get_all_students(db: AsyncSession = Depends(get_db)):
    """Retrieve all students from the database."""

    # Build a SQL query: SELECT * FROM students
    query = select(Student)

    # Execute the query
    result = await db.execute(query)

    # Extract all student rows
    students = result.scalars().all()

    return students


# =============================================
# GET /students/{id} — Fetch a single student
# =============================================
@router.get("/{student_id}", response_model=StudentResponse)
async def get_student(student_id: int, db: AsyncSession = Depends(get_db)):
    """Retrieve a single student by their ID."""

    # Build query: SELECT * FROM students WHERE id = ?
    query = select(Student).where(Student.id == student_id)
    result = await db.execute(query)
    student = result.scalar_one_or_none()

    # If student not found, return 404 error
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


# =============================================
# POST /students — Add a new student
# =============================================
@router.post("/", response_model=StudentResponse, status_code=201)
async def create_student(data: StudentCreate, db: AsyncSession = Depends(get_db)):
    """Add a new student to the database."""

    # Create a new Student object from the request data
    new_student = Student(
        name=data.name,
        email=data.email,
        age=data.age
    )

    # Add to the session and save to database
    db.add(new_student)
    await db.commit()

    # Refresh to get the auto-generated ID and created_at
    await db.refresh(new_student)

    return new_student


# =============================================
# DELETE /students/{id} — Remove a student
# =============================================
@router.delete("/{student_id}", status_code=204)
async def delete_student(student_id: int, db: AsyncSession = Depends(get_db)):
    """Delete a student by their ID."""

    # First, find the student
    query = select(Student).where(Student.id == student_id)
    result = await db.execute(query)
    student = result.scalar_one_or_none()

    # If student not found, return 404 error
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    # Delete the student
    await db.delete(student)
    await db.commit()

    # 204 No Content — nothing to return
    return None
