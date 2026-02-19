# 🎯 Workshop Coding Tasks

Complete the following tasks to build the Student Management System.

---

## ✅ Backend Tasks
Open the `starter/backend` folder and complete these tasks:

1. [ ] **Complete StudentCreate schema** in `schemas.py`
   - Add `name`, `email`, and `age` fields with proper validation.
2. [ ] **Add POST /students endpoint** in `routes.py`
   - Implement the logic to create a new student in the database.
3. [ ] **Add DELETE /students/{id} endpoint** in `routes.py`
   - Implement the logic to remove a student from the database.

---

## ✅ Frontend Tasks
Open the `starter/frontend` folder and complete these tasks:

4. [ ] **Implement addStudent() function** in `main.ts`
   - Write the `fetch` call to send a POST request to the backend.
5. [ ] **Implement deleteStudent() function** in `main.ts`
   - Write the `fetch` call to send a DELETE request.
6. [ ] **Add delete button** in `renderStudents()` function
   - Add the HTML button element for each student card.
7. [ ] **Uncomment handleDelete** at the bottom of `main.ts`
   - Enable the click handler to connect the UI to your code.

---

### 🚀 Success Criteria
- You can add a student thru the UI.
- The student appears in the list.
- You can delete a student from the list.
