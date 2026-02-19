# 🛠️ StackBridge – Setup Instructions (Windows)

Step-by-step guide to get StackBridge running on Windows 10/11.

---

## Prerequisites

| Software | Version | Download |
|----------|---------|----------|
| Python | 3.11+ | https://www.python.org/downloads/ |
| Node.js | 20+ | https://nodejs.org/ |
| PostgreSQL | 16+ | https://www.postgresql.org/download/windows/ |
| VS Code | Latest | https://code.visualstudio.com/ |

> **Important:** When installing Python, check ✅ **"Add Python to PATH"**
> When installing Node.js, check ✅ **"Add to PATH"**

---

## Step 1: Fix PowerShell Execution Policy

Open PowerShell and run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Type `Y` and press Enter.

---

## Step 2: Create the PostgreSQL Database

Open PowerShell and run:

```powershell
psql -U postgres
```

Enter your PostgreSQL password, then run:

```sql
CREATE DATABASE stackbridge;
\q
```

---

## Step 3: Setup Backend

```powershell
# Navigate to the backend folder
cd d:\Vikash\My Projects\rkmvc-workshop\complete\backend

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file from example
copy .env.example .env
```

Edit `.env` if your PostgreSQL password is different from `postgres`:

```
DATABASE_URL=postgresql+asyncpg://postgres:YOUR_PASSWORD@localhost:5432/stackbridge
```

---

## Step 4: Run Backend

```powershell
# Make sure venv is activated (you see "(venv)" in your prompt)
uvicorn main:app --reload
```

✅ **Verify:** Open http://localhost:8000/docs in your browser. You should see the Swagger UI.

---

## Step 5: Setup Frontend

Open a **new** PowerShell window:

```powershell
# Navigate to the frontend folder
cd d:\Vikash\My Projects\rkmvc-workshop\complete\frontend

# Install dependencies
npm install
```

---

## Step 6: Run Frontend

```powershell
npm run dev
```

✅ **Verify:** Open http://localhost:5173 in your browser. You should see the StackBridge UI.

---

## Step 7: Test End-to-End

1. Open the frontend at http://localhost:5173
2. Fill in the form: Name, Email, Age
3. Click "Add Student"
4. Click "Refresh" to see the student list
5. Click "Delete" to remove a student

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `running scripts is disabled` | Run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| `connection refused` | Start PostgreSQL service: `net start postgresql-x64-17` |
| `database "stackbridge" does not exist` | Run: `psql -U postgres` then `CREATE DATABASE stackbridge;` |
| `ModuleNotFoundError` | Activate venv: `.\venv\Scripts\activate` then `pip install -r requirements.txt` |
| `Address already in use` | Use different port: `uvicorn main:app --reload --port 8001` |
| `'npm' is not recognized` | Restart terminal after installing Node.js |
