# 🎓 StackBridge – Instructor Guide

## Workshop Overview

| Detail | Value |
|--------|-------|
| **Duration** | 5 hours |
| **Students** | ~100 final-year BCA students |
| **Level** | Beginner to Intermediate |
| **Environment** | Windows 10/11, Computer Lab |
| **Tech Stack** | FastAPI, SQLAlchemy, PostgreSQL, TypeScript, Vite |

---

## 📋 5-Hour Time Allocation

| Time | Duration | Activity |
|------|----------|----------|
| **0:00 – 0:30** | 30 min | Welcome + Environment Setup |
| **0:30 – 1:00** | 30 min | Theory: REST APIs, ORM, Architecture |
| **1:00 – 1:45** | 45 min | Live Coding: Backend (config → models → routes) |
| **1:45 – 2:00** | 15 min | ☕ **Break** |
| **2:00 – 2:30** | 30 min | Live Coding: Frontend (HTML + Fetch API) |
| **2:30 – 3:15** | 45 min | Student Task: Complete Starter Project (Backend) |
| **3:15 – 3:30** | 15 min | ☕ **Break** |
| **3:30 – 4:15** | 45 min | Student Task: Complete Starter Project (Frontend) |
| **4:15 – 4:45** | 30 min | Debugging Help + Student Demos |
| **4:45 – 5:00** | 15 min | Wrap-up + Q&A + Next Steps |

---

## 🎙️ Part 1: What to Explain (Theory — 30 min)

### REST APIs (5 min)
> "Think of a REST API like a waiter in a restaurant. You (the frontend) place an order. The waiter (API) takes it to the kitchen (backend). The kitchen prepares the food (database query) and the waiter brings it back."

| HTTP Method | Path | What it does |
|-------------|------|-------------|
| `GET` | `/students` | Get all students |
| `GET` | `/students/5` | Get student #5 |
| `POST` | `/students` | Add a new student |
| `DELETE` | `/students/5` | Delete student #5 |

### ORM (5 min)
> "Without ORM, you write raw SQL: `SELECT * FROM students`. With ORM, you write Python: `select(Student)`. Same result, but the Python way is safer and easier to maintain."

### Async/Await (5 min)
> "When you order food online, you don't stand at the door waiting. You do other things and get notified when it arrives. That's what `async/await` does — the server can handle other requests while waiting for the database."

### CORS (3 min)
> "Browsers block requests between different URLs by default. CORS is like a security badge — it tells the browser 'this frontend is allowed to talk to this backend.'"

### Layered Architecture (5 min)
Draw this on the whiteboard:
```
Frontend (TypeScript)  →  API Routes (FastAPI)  →  Database (PostgreSQL)
     UI + Fetch             Business Logic            Data Storage
                                 ↓
                          Schemas (Pydantic) = Validation
                          Models (SQLAlchemy) = Table Structure
```

### Project Structure (7 min)
Walk through the folder structure:
```
backend/
├── config.py      ← "Where does the database live?"
├── database.py    ← "How do we connect to it?"
├── models.py      ← "What does our data look like?"
├── schemas.py     ← "What rules must the data follow?"
├── routes.py      ← "What can the API do?"
└── main.py        ← "Start everything!"
```

---

## 💻 Part 2: Live Coding Flow (75 min total)

### Step-by-step: What to Code Live

**Phase 1: Backend (45 min)**

Code these files **in this order** (each builds on the previous):

1. **`config.py`** (3 min) — Show `.env` loading
2. **`database.py`** (8 min) — Explain engine, session, `get_db()`
3. **`models.py`** (7 min) — Build the Student table
4. **`schemas.py`** (7 min) — Show request/response validation
5. **`routes.py`** (12 min) — Build GET first, then POST, then DELETE
6. **`main.py`** (8 min) — Wire it all together, show CORS

🔴 **Checkpoint 1:** Run the backend, open Swagger at `http://localhost:8000/docs`, demo all 4 endpoints live.

**Phase 2: Frontend (30 min)**

1. **`index.html`** (5 min) — Build the form and list structure
2. **`style.css`** (5 min) — Quick walkthrough, don't type the whole thing (give it pre-made)
3. **`main.ts`** (20 min) — Code `fetchStudents()` live, explain Fetch API

🔴 **Checkpoint 2:** Run the frontend, show the form, fetch students from the API.

---

## 📦 Part 3: When to Distribute Starter Code

| When | What to Distribute |
|------|--------------------|
| **After live coding demo** (at ~2:30) | Distribute the `starter/` folder |
| **Tell students** | "Your backend GET endpoints work. Your job is to add POST and DELETE." |
| **Give them the checklist** | See below |

### Student Checklist (Write on Board)

```
✅ Backend Tasks:
  1. Complete StudentCreate schema in schemas.py (add name, email, age fields)
  2. Add POST /students endpoint in routes.py
  3. Add DELETE /students/{id} endpoint in routes.py

✅ Frontend Tasks:
  4. Implement addStudent() function in main.ts
  5. Implement deleteStudent() function in main.ts
  6. Add delete button in renderStudents() function
  7. Uncomment handleDelete at the bottom of main.ts
```

---

## ⚠️ Common Lab Errors & Fixes

### 1. Virtual Environment Won't Activate

**Error:** `running scripts is disabled on this system`

**Fix:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then retry: `.\venv\Scripts\activate`

---

### 2. PostgreSQL Not Running

**Error:** `connection refused` or `could not connect to server`

**Fix:**
1. Open **Services** (`Win + R` → `services.msc`)
2. Find **postgresql-x64-XX**
3. Right-click → **Start**

Or run in PowerShell (as Admin):
```powershell
net start postgresql-x64-17
```

---

### 3. Database Does Not Exist

**Error:** `database "stackbridge" does not exist`

**Fix:**
```powershell
psql -U postgres
CREATE DATABASE stackbridge;
\q
```

---

### 4. Port Already in Use

**Error:** `[Errno 10048]` or `Address already in use`

**Fix:**
```powershell
# Find what's using port 8000
netstat -ano | findstr :8000
# Kill the process (replace PID)
taskkill /PID <PID> /F
```

Or just use a different port:
```powershell
uvicorn main:app --reload --port 8001
```

---

### 5. CORS Error in Browser Console

**Error:** `Access to fetch has been blocked by CORS policy`

**Fix:** Make sure `main.py` has the CORS middleware configured. If students are running their own backend, ensure they have the CORS block in their `main.py`.

---

### 6. Module Not Found

**Error:** `ModuleNotFoundError: No module named 'fastapi'`

**Fix:**
```powershell
# Make sure venv is activated (you should see (venv) in your prompt)
.\venv\Scripts\activate
pip install -r requirements.txt
```

---

### 7. npm/Node Not Recognized

**Error:** `'npm' is not recognized`

**Fix:** Restart the terminal after installing Node.js. If still not working:
```powershell
# Check if Node is in PATH
$env:Path
# If not, add it manually or reinstall Node with "Add to PATH" checked
```

---

### 8. TypeScript Errors

**Error:** `Cannot find module './style.css'`

**This is normal!** Vite handles CSS imports at build time. The app still runs correctly with `npm run dev`.

---

## 🏫 Managing 100 Students in a Lab

### Before the Workshop
- [ ] Pre-install Python 3.11+, Node.js 20+, PostgreSQL 16+ on ALL machines
- [ ] Pre-create the `stackbridge` database on all machines
- [ ] Copy the `starter/` folder to all desktops
- [ ] Test one machine end-to-end yourself
- [ ] Set PowerShell execution policy on all machines
- [ ] Print a one-page "Quick Reference" handout with commands

### During the Workshop
- **Use 2-3 Teaching Assistants** (TAs) — one per ~35 students
- **Put commands on a shared screen** (projector) — students type along
- **Use a "traffic light" system**: Students put a GREEN sticky note on their monitor if they're fine, RED if they need help
- **Don't wait** for everyone to finish each step — move on when ~80% are done, TAs help the rest

### Dealing with Setup Failures
- **Have a "rescue USB"** with pre-configured `venv/` and `node_modules/` folders
- **Pair slow machines** — two students can share one working machine
- **If PostgreSQL won't start**: Let students use the instructor's database by changing their `.env` URL to point to your machine's IP

---

## 📝 Quick Reference Card (Print for Students)

```
================================
  StackBridge Quick Reference
================================

--- BACKEND ---
cd starter/backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn main:app --reload

API Docs: http://localhost:8000/docs

--- FRONTEND ---
cd starter/frontend
npm install
npm run dev

App: http://localhost:5173

--- USEFUL ---
Ctrl+C = Stop server
Check DB: psql -U postgres -d stackbridge
================================
```

---

## 📊 Example API Requests & Responses

### POST /students — Add a Student

**Request:**
```json
{
  "name": "Rahul Kumar",
  "email": "rahul@example.com",
  "age": 21
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "name": "Rahul Kumar",
  "email": "rahul@example.com",
  "age": 21,
  "created_at": "2026-02-18T14:30:00"
}
```

### GET /students — Get All Students

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "name": "Rahul Kumar",
    "email": "rahul@example.com",
    "age": 21,
    "created_at": "2026-02-18T14:30:00"
  },
  {
    "id": 2,
    "name": "Priya Singh",
    "email": "priya@example.com",
    "age": 22,
    "created_at": "2026-02-18T14:31:00"
  }
]
```

### GET /students/1 — Get Student by ID

**Response (200 OK):**
```json
{
  "id": 1,
  "name": "Rahul Kumar",
  "email": "rahul@example.com",
  "age": 21,
  "created_at": "2026-02-18T14:30:00"
}
```

### DELETE /students/1 — Delete a Student

**Response:** `204 No Content` (empty body)

### Error — Student Not Found

**Response (404):**
```json
{
  "detail": "Student not found"
}
```

### Error — Validation Failed

**Response (422):**
```json
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

---

## 🎯 Success Criteria

By the end of the workshop, each student should have:

1. ✅ A running FastAPI backend with 4 endpoints
2. ✅ A running Vite + TypeScript frontend
3. ✅ The ability to add, view, and delete students through the UI
4. ✅ Understanding of: REST APIs, ORM, Frontend-Backend communication

**Good luck! You've got this. 🚀**
