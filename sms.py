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
# View all students


def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if len(students) == 0:
        print("No students found!")
    else:
        print("\n--- Student List ---")
        print(f"{'ID':<5} {'Name':<20} {'Age':<5} {'Grade':<5}")
        print("-" * 35)
        for student in students:
            print(
                f"{student[0]:<5} {student[1]:<20} {student[2]:<5} {student[3]:<5}")
        print("-" * 35)


# Run
add_student()
view_students()
conn.close()
