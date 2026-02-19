"""
main.py - Application Entry Point
------------------------------------
✅ This file is COMPLETE. No changes needed.

Run with: uvicorn main:app --reload
Swagger docs: http://localhost:8000/docs
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Database tables created successfully!")
    yield
    print("👋 Application shutting down...")


app = FastAPI(
    title="StackBridge – Student Management System",
    description="A simple REST API for managing student records.",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/", tags=["Health"])
async def health_check():
    return {"status": "ok", "message": "StackBridge API is running! 🚀"}
