import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT    NOT NULL,
    age     INTEGER,
    grade   TEXT
)
""")
conn.commit()

# Insert student


def add_student():
    name = input("Enter name  : ")
    age = input("Enter age   : ")
    grade = input("Enter grade : ")

    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
                   (name, age, grade))
    conn.commit()
    print("✅ Student added successfully!")


# Run
add_student()
conn.close()
