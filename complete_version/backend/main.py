"""
main.py - Application Entry Point
------------------------------------
This is where the FastAPI application starts.
It wires everything together:
1. Creates the FastAPI app
2. Enables CORS (so the frontend can talk to the backend)
3. Creates database tables on startup
4. Includes all API routes

Run with: uvicorn main:app --reload
Swagger docs: http://localhost:8000/docs
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routes import router


# --- Lifespan: runs on app startup and shutdown ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    On startup: Create all database tables if they don't exist.
    This is equivalent to running CREATE TABLE IF NOT EXISTS.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Database tables created successfully!")
    yield  # App runs here
    print("👋 Application shutting down...")


# --- Create the FastAPI application ---
app = FastAPI(
    title="StackBridge – Student Management System",
    description="A simple REST API for managing student records. Built with FastAPI + PostgreSQL.",
    version="1.0.0",
    lifespan=lifespan,
)


# --- CORS Configuration ---
# CORS (Cross-Origin Resource Sharing) allows the frontend
# (running on a different port) to make requests to this API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Allow all origins (fine for development)
    allow_credentials=True,
    allow_methods=["*"],       # Allow all HTTP methods (GET, POST, DELETE, etc.)
    allow_headers=["*"],       # Allow all headers
)


# --- Include our routes ---
app.include_router(router)


# --- Health check endpoint ---
@app.get("/", tags=["Health"])
async def health_check():
    """Simple endpoint to verify the API is running."""
    return {"status": "ok", "message": "StackBridge API is running! 🚀"}
