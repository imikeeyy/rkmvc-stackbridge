"""
routes.py - API Endpoints
---------------------------
GET /students is provided as a working example.

# TODO: STUDENT TASK — Add POST and DELETE endpoints
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import get_db
from models import Student
from schemas import StudentCreate, StudentResponse

router = APIRouter(prefix="/students", tags=["Students"])


# =============================================
# ✅ EXAMPLE — GET /students (WORKING)
# =============================================
@router.get("/", response_model=list[StudentResponse])
async def get_all_students(db: AsyncSession = Depends(get_db)):
    """Retrieve all students from the database."""
    query = select(Student)
    result = await db.execute(query)
    students = result.scalars().all()
    return students


# =============================================
# ✅ PROVIDED — GET /students/{id}
# =============================================
@router.get("/{student_id}", response_model=StudentResponse)
async def get_student(student_id: int, db: AsyncSession = Depends(get_db)):
    """Retrieve a single student by their ID."""
    query = select(Student).where(Student.id == student_id)
    result = await db.execute(query)
    student = result.scalar_one_or_none()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


# =============================================
# TODO: STUDENT TASK — POST /students
# =============================================
# Create a new endpoint that:
# 1. Accepts StudentCreate data
# 2. Creates a new Student object
# 3. Adds it to the database
# 4. Returns the created student with status code 201
#
# Hints:
# - Use @router.post("/", response_model=StudentResponse, status_code=201)
# - Create: new_student = Student(name=data.name, email=data.email, age=data.age)
# - Save:  db.add(new_student) → await db.commit() → await db.refresh(new_student)
#
# Write your code below:
# @router.post(...)
# async def create_student(...):
#     ...


# =============================================
# TODO: STUDENT TASK — DELETE /students/{id}
# =============================================
# Create a new endpoint that:
# 1. Finds a student by ID
# 2. If not found, raise HTTPException(status_code=404, detail="Student not found")
# 3. Deletes the student from the database
# 4. Returns status code 204 (No Content)
#
# Hints:
# - Use @router.delete("/{student_id}", status_code=204)
# - Find:   use select() + where() like in get_student above
# - Delete: await db.delete(student) → await db.commit()
#
# Write your code below:
# @router.delete(...)
# async def delete_student(...):
#     ...
