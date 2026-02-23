/**
 * main.ts - Frontend Application Logic (STARTER VERSION)
 * -------------------------------------------------------
 * fetchStudents() is provided as a working example.
 *
 * # TODO: STUDENT TASK — Complete addStudent(), deleteStudent(), and delete button rendering
 */

import "./style.css";

// ==============================================
// CONFIGURATION
// ==============================================
const API_URL = "http://localhost:8000/students";

// ==============================================
// TYPE DEFINITIONS
// ==============================================
interface Student {
    id: number;
    name: string;
    email: string;
    age: number;
    created_at: string;
}

interface StudentCreate {
    name: string;
    email: string;
    age: number;
}

// ==============================================
// DOM ELEMENT REFERENCES
// ==============================================
const form = document.getElementById("student-form") as HTMLFormElement;
const nameInput = document.getElementById("name") as HTMLInputElement;
const emailInput = document.getElementById("email") as HTMLInputElement;
const ageInput = document.getElementById("age") as HTMLInputElement;
const studentList = document.getElementById("student-list") as HTMLDivElement;
const refreshBtn = document.getElementById("refresh-btn") as HTMLButtonElement;
const formMessage = document.getElementById("form-message") as HTMLDivElement;

// ==============================================
// ✅ PROVIDED — Fetch All Students (WORKING)
// ==============================================
async function fetchStudents(): Promise<void> {
    try {
        studentList.innerHTML = '<p class="loading">⏳ Loading students...</p>';
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }
        const students: Student[] = await response.json();
        renderStudents(students);
    } catch (error) {
        studentList.innerHTML = `<p class="error">❌ Failed to load students. Is the backend running?</p>`;
        console.error("Fetch error:", error);
    }
}

// ==============================================
// TODO: STUDENT TASK — Add a New Student
// ==============================================
/**
 * Send a POST request to add a new student.
 *
 * Steps:
 * 1. Use fetch() with method "POST"
 * 2. Set headers: { "Content-Type": "application/json" }
 * 3. Set body: JSON.stringify(data)
 * 4. Check if response.ok
 * 5. Return true on success, false on failure
 *
 * Example:
 *   const response = await fetch(API_URL + "/", {
 *     method: "POST",
 *     headers: { "Content-Type": "application/json" },
 *     body: JSON.stringify(data),
 *   });
 */
async function addStudent(data: StudentCreate): Promise<boolean> {
    // TODO: STUDENT TASK — Implement this function
    // Remove the line below and write your code
    console.log("addStudent not implemented yet!", data);
    showMessage("❌ addStudent() is not implemented yet. Check main.ts!", "error");
    return false;
}

// ==============================================
// TODO: STUDENT TASK — Delete a Student
// ==============================================
/**
 * Send a DELETE request to remove a student.
 *
 * Steps:
 * 1. Use fetch() with method "DELETE"
 * 2. URL should be: `${API_URL}/${id}`
 * 3. Check if response.ok
 * 4. Return true on success, false on failure
 */
async function deleteStudent(id: number): Promise<boolean> {
    // TODO: STUDENT TASK — Implement this function
    console.log("deleteStudent not implemented yet!", id);
    showMessage("❌ deleteStudent() is not implemented yet. Check main.ts!", "error");
    return false;
}

// ==============================================
// UI RENDERING
// ==============================================
function renderStudents(students: Student[]): void {
    if (students.length === 0) {
        studentList.innerHTML = '<p class="empty-state">📭 No students found. Add one above!</p>';
        return;
    }

    // TODO: STUDENT TASK — Add a delete button to each student card
    // Currently there is NO delete button. After implementing deleteStudent(),
    // add a button like this inside each student-card:
    //   <button class="btn btn-danger" onclick="handleDelete(${student.id})">🗑️ Delete</button>

    const html = students
        .map(
            (student) => `
      <div class="student-card">
        <div class="student-info">
          <h3>${escapeHtml(student.name)}</h3>
          <p>📧 ${escapeHtml(student.email)}</p>
          <p>🎂 Age: ${student.age}</p>
          <p class="date">Added: ${new Date(student.created_at).toLocaleDateString()}</p>
        </div>
        <!-- TODO: STUDENT TASK — Add delete button here -->
      </div>
    `
        )
        .join("");

    studentList.innerHTML = html;
}

function showMessage(text: string, type: "success" | "error"): void {
    formMessage.textContent = text;
    formMessage.className = `message ${type}`;
    formMessage.classList.remove("hidden");
    setTimeout(() => {
        formMessage.classList.add("hidden");
    }, 4000);
}

function escapeHtml(text: string): string {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
}

// ==============================================
// EVENT HANDLERS
// ==============================================
form.addEventListener("submit", async (e: Event) => {
    e.preventDefault();

    const data: StudentCreate = {
        name: nameInput.value.trim(),
        email: emailInput.value.trim(),
        age: parseInt(ageInput.value),
    };

    if (!data.name || !data.email || isNaN(data.age)) {
        showMessage("❌ Please fill in all fields correctly.", "error");
        return;
    }

    const success = await addStudent(data);

    if (success) {
        showMessage("✅ Student added successfully!", "success");
        form.reset();
        await fetchStudents();
    }
});

refreshBtn.addEventListener("click", () => {
    fetchStudents();
});

// TODO: STUDENT TASK — Uncomment and use this after implementing deleteStudent()
// (window as any).handleDelete = async (id: number) => {
//   if (!confirm("Are you sure you want to delete this student?")) return;
//   const success = await deleteStudent(id);
//   if (success) {
//     showMessage("✅ Student deleted!", "success");
//     await fetchStudents();
//   }
// };

// ==============================================
// INITIAL LOAD
// ==============================================
fetchStudents();
