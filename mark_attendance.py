import sqlite3
from datetime import date

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

student_id = input("Enter student ID: ")
status = input("Enter status (Present/Absent): ").capitalize()
today = date.today().isoformat()

cursor.execute("""
    INSERT INTO attendance (student_id, date, status)
    VALUES (?, ?, ?)
""", (student_id, today, status))

conn.commit()
print(f"✅ Attendance marked as '{status}' for Student ID {student_id} on {today}")
conn.close()
