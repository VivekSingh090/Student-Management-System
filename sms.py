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
# Search student


def search_student():
    name = input("Enter name to search: ")
    cursor.execute("SELECT * FROM students WHERE name LIKE ?",
                   ('%' + name + '%',))
    students = cursor.fetchall()

    if len(students) == 0:
        print("❌ No student found!")
    else:
        print("\n--- Search Results ---")
        print(f"{'ID':<5} {'Name':<20} {'Age':<5} {'Grade':<5}")
        print("-" * 35)
        for student in students:
            print(
                f"{student[0]:<5} {student[1]:<20} {student[2]:<5} {student[3]:<5}")
        print("-" * 35)


# Run
add_student()
view_students()
search_student()
# Update student


def update_student():
    view_students()
    id = input("Enter student ID to update: ")
    name = input("Enter new name  : ")
    age = input("Enter new age   : ")
    grade = input("Enter new grade : ")

    cursor.execute("UPDATE students SET name=?, age=?, grade=? WHERE id=?",
                   (name, age, grade, id))
    conn.commit()
    print("✅ Student updated successfully!")


# Run
add_student()
view_students()
search_student()
update_student()
# Delete student


def delete_student():
    view_students()
    id = input("Enter student ID to delete: ")

    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    print("✅ Student deleted successfully!")

    # Run
# CLI Menu


def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Goodbye! 👋")
            conn.close()
            break
        else:
            print("❌ Invalid choice! Please try again.")


# Run
menu()
