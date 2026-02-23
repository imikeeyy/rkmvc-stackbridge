# 🎓 StackBridge – Student Management System

A full-stack workshop project for BCA students. Built with **FastAPI** + **PostgreSQL** + **TypeScript** + **Vite**.

---

## 📂 Project Structure

```
rkmvc-workshop/
├── complete/          ← Full working solution (instructor reference)
│   ├── backend/       ← FastAPI + SQLAlchemy + PostgreSQL
│   └── frontend/      ← Vite + TypeScript (vanilla)
├── starter/           ← Student starter code (with TODOs)
│   ├── backend/       ← GET endpoints work, POST + DELETE are TODOs
│   └── frontend/      ← Fetch works, add/delete are TODOs
├── INSTRUCTOR_GUIDE.md ← Teaching flow, time plan, troubleshooting
├── SETUP.md            ← Windows step-by-step setup
└── README.md           ← This file
```

## 🚀 Quick Start

### Backend
```powershell
cd complete/backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn main:app --reload
```
API Docs → http://localhost:8000/docs

### Frontend
```powershell
cd complete/frontend
npm install
npm run dev
```
App → http://localhost:5173

## 📖 Documentation

- **[SETUP.md](./SETUP.md)** — Detailed setup instructions
- **[INSTRUCTOR_GUIDE.md](./INSTRUCTOR_GUIDE.md)** — Full teaching guide

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | TypeScript, Vite, HTML, CSS |
| Backend | Python, FastAPI, Pydantic |
| Database | PostgreSQL, SQLAlchemy (async) |
| Tools | Uvicorn, asyncpg, python-dotenv |
