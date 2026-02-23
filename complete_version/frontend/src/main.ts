/**
 * main.ts - Frontend Application Logic
 * --------------------------------------
 * This file handles all interactions between the UI and the backend API.
 *
 * Key concepts:
 * - Fetch API: Built-in browser function to make HTTP requests
 * - async/await: Makes asynchronous code look synchronous
 * - DOM manipulation: Updating the HTML page with JavaScript
 */

import "./style.css";

// ==============================================
// CONFIGURATION
// ==============================================

// Backend API base URL (FastAPI runs on port 8000 by default)
const API_URL = "http://localhost:8000/students";

// ==============================================
// TYPE DEFINITIONS
// ==============================================

/** Shape of a student object returned from the API */
interface Student {
    id: number;
    name: string;
    email: string;
    age: number;
    created_at: string;
}

/** Shape of the data we send when creating a student */
interface StudentCreate {
    name: string;
    email: string;
    age: number;
}

// ==============================================
// DOM ELEMENT REFERENCES
// ==============================================

// Get references to HTML elements we need to interact with
const form = document.getElementById("student-form") as HTMLFormElement;
const nameInput = document.getElementById("name") as HTMLInputElement;
const emailInput = document.getElementById("email") as HTMLInputElement;
const ageInput = document.getElementById("age") as HTMLInputElement;
const studentList = document.getElementById("student-list") as HTMLDivElement;
const refreshBtn = document.getElementById("refresh-btn") as HTMLButtonElement;
const formMessage = document.getElementById("form-message") as HTMLDivElement;

// ==============================================
// API FUNCTIONS
// ==============================================

/**
 * Fetch all students from the backend API.
 * Makes a GET request to /students
 */
async function fetchStudents(): Promise<void> {
    try {
        // Show loading state
        studentList.innerHTML = '<p class="loading">⏳ Loading students...</p>';

        // Make the GET request
        const response = await fetch(API_URL);

        // Check if the request was successful
        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        // Parse the JSON response
        const students: Student[] = await response.json();

        // Render the students in the UI
        renderStudents(students);
    } catch (error) {
        // Show error to the user
        studentList.innerHTML = `<p class="error">❌ Failed to load students. Is the backend running?</p>`;
        console.error("Fetch error:", error);
    }
}

/**
 * Add a new student by sending data to the backend API.
 * Makes a POST request to /students
 */
async function addStudent(data: StudentCreate): Promise<boolean> {
    try {
        const response = await fetch(API_URL + "/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json", // Tell the API we're sending JSON
            },
            body: JSON.stringify(data), // Convert our object to a JSON string
        });

        // Check if creation was successful (201 Created)
        // if (!response.ok) {
        //     const errorData = await response.json();
        //     // Show validation errors from the API
        //     const detail = errorData.detail;
        //     if (Array.isArray(detail)) {
        //         throw new Error(detail.map((e: any) => e.msg).join(", "));
        //     }
        //     throw new Error(typeof detail === "string" ? detail : "Failed to add student");
        // }

        return true;
    } catch (error) {
        showMessage(`❌ ${(error as Error).message}`, "error");
        console.error("Add student error:", error);
        return false;
    }
}

/**
 * Delete a student by their ID.
 * Makes a DELETE request to /students/{id}
 */
async function deleteStudent(id: number): Promise<boolean> {
    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: "DELETE",
        });

        if (!response.ok) {
            throw new Error(`Failed to delete student (status ${response.status})`);
        }

        return true;
    } catch (error) {
        showMessage(`❌ ${(error as Error).message}`, "error");
        console.error("Delete error:", error);
        return false;
    }
}

// ==============================================
// UI RENDERING FUNCTIONS
// ==============================================

/**
 * Render the list of students in the UI.
 * Creates HTML elements for each student.
 */
function renderStudents(students: Student[]): void {
    // Handle empty list
    if (students.length === 0) {
        studentList.innerHTML = '<p class="empty-state">📭 No students found. Add one above!</p>';
        return;
    }

    // Build HTML for each student
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
        <button class="btn btn-danger" onclick="handleDelete(${student.id})">
          🗑️ Delete
        </button>
      </div>
    `
        )
        .join("");

    studentList.innerHTML = html;
}

/**
 * Show a success or error message below the form.
 */
function showMessage(text: string, type: "success" | "error"): void {
    formMessage.textContent = text;
    formMessage.className = `message ${type}`;
    formMessage.classList.remove("hidden");

    // Auto-hide after 4 seconds
    setTimeout(() => {
        formMessage.classList.add("hidden");
    }, 4000);
}

/**
 * Prevent XSS attacks by escaping HTML characters.
 * This is important when displaying user-provided data!
 */
function escapeHtml(text: string): string {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
}

// ==============================================
// EVENT HANDLERS
// ==============================================

/**
 * Handle form submission — adds a new student.
 */
form.addEventListener("submit", async (e: Event) => {
    e.preventDefault(); // Prevent page reload

    // Gather form data
    const data: StudentCreate = {
        name: nameInput.value.trim(),
        email: emailInput.value.trim(),
        age: parseInt(ageInput.value),
    };

    // Validate on client side
    if (!data.name || !data.email || isNaN(data.age)) {
        showMessage("❌ Please fill in all fields correctly.", "error");
        return;
    }

    // Send to API
    const success = await addStudent(data);

    if (success) {
        showMessage("✅ Student added successfully!", "success");
        form.reset();        // Clear the form
        await fetchStudents(); // Refresh the student list
    }
});

/**
 * Handle refresh button click.
 */
refreshBtn.addEventListener("click", () => {
    fetchStudents();
});

/**
 * Handle delete button click.
 * This function is called from the inline onclick in renderStudents().
 */
(window as any).handleDelete = async (id: number) => {
    // Confirm before deleting
    if (!confirm("Are you sure you want to delete this student?")) {
        return;
    }

    const success = await deleteStudent(id);

    if (success) {
        showMessage("✅ Student deleted successfully!", "success");
        await fetchStudents(); // Refresh the list
    }
};

// ==============================================
// INITIAL LOAD
// ==============================================

// Load students when the page first opens
fetchStudents();
