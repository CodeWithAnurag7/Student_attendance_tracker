import sqlite3
from datetime import date

DB_PATH = "/Users/anuragyadav/Documents/Projects/Student_attendacne_tracker/database/students.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

# ---------------- Functions ---------------- #

def add_student(name, roll_number, course):
    """Naya student add kare"""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO students (name, roll_number, course)
            VALUES (?, ?, ?)
        """, (name, roll_number, course))
        conn.commit()
        print(f"Student '{name}' added successfully!")
    except sqlite3.IntegrityError:
        print(f"Error: Roll number '{roll_number}' already exists!")
    finally:
        conn.close()

def mark_attendance(student_id, status):
    """Student ka attendance mark kare"""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO attendance (student_id, date, status)
            VALUES (?, ?, ?)
        """, (student_id, date.today(), status))
        conn.commit()
        print(f"Attendance for student_id={student_id} marked as '{status}'")
    except sqlite3.IntegrityError:
        print(f"Error: student_id {student_id} does not exist!")
    finally:
        conn.close()

def view_students():
    """Saare students list kare"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    if students:
        print("Students List:")
        for s in students:
            print(f"ID: {s[0]}, Name: {s[1]}, Roll: {s[2]}, Course: {s[3]}")
    else:
        print("No students found!")

def view_attendance():
    """Attendance records dikhaye"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.id, s.name, s.roll_number, a.date, a.status
        FROM attendance a
        JOIN students s ON a.student_id = s.id
    """)
    records = cursor.fetchall()
    conn.close()
    if records:
        print("Attendance Records:")
        for r in records:
            print(f"ID: {r[0]}, Name: {r[1]}, Roll: {r[2]}, Date: {r[3]}, Status: {r[4]}")
    else:
        print("No attendance records found!")

# ---------------- Example Usage ---------------- #

if __name__ == "__main__":
    # Example: Add students
    add_student("Anurag Yadav", "B23", "Computer Science")
    add_student("Rahul Kumar", "B24", "Mechanical")

    # Example: Mark attendance
    mark_attendance(1, "Present")
    mark_attendance(2, "Absent")

    # Example: View data
    view_students()
    view_attendance()