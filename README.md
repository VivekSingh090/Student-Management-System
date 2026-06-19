# 🎓 Student Management System (SMS)

A command-line application built with **Python** and **SQLite** to manage student records.  
This project demonstrates core skills in Python programming, SQL database operations, and CLI application design.

---

## 📌 Features

- ➕ Add new student records
- 📋 View all students
- 🔍 Search student by name or ID
- ✏️ Update student details
- 🗑️ Delete student records
- 🖥️ Interactive CLI menu for easy navigation

---

## 🛠️ Tech Stack

| Tool       | Purpose                        |
|------------|-------------------------------|
| Python 3.x | Core programming language      |
| SQLite3    | Lightweight local database     |
| VS Code    | Development environment        |

---

## 📁 Project Structure

```
student-management-system/
│
├── sms.py          # Main application file
├── schema.sql      # Database schema (CREATE TABLE script)
├── .gitignore      # Ignores .db files
└── README.md       # Project documentation
```

---

## ⚙️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/student-management-system.git
cd student-management-system
```

### 2. Make sure Python is installed
```bash
python --version
```

### 3. Run the application
```bash
python sms.py
```

> The SQLite database (`students.db`) will be created automatically on first run.

---

## 🗄️ Database Schema

```sql
CREATE TABLE IF NOT EXISTS students (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT    NOT NULL,
    age     INTEGER,
    grade   TEXT
);
```

---

## 📷 Sample Output

```
===== Student Management System =====
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
Enter your choice: 
```

---

## 📚 What I Learned

- Connecting Python to a SQLite database using the `sqlite3` module
- Writing and executing SQL queries (CREATE, INSERT, SELECT, UPDATE, DELETE)
- Building a user-friendly CLI menu using Python
- Structuring a project for version control with Git

---

## 🚀 Future Improvements

- [ ] Add input validation and error handling
- [ ] Export student data to CSV
- [ ] Build a simple web interface using Flask
- [ ] Connect to MySQL for production-level database

---

## 👨‍💻 Author

**Vivek**  
Diploma in Computer Science (2024)  
📍 Noida / Delhi NCR, India  
🔗 [LinkedIn](https://linkedin.com/in/your-profile) | [GitHub](https://github.com/VivekSingh090)

---

> 💡 *This project is part of my portfolio as I pursue roles in Python Development and Data Analytics.*