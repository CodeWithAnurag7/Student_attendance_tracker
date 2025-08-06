import sqlite3

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

name = input("Enter student name: ")
roll_number = input("Enter student roll number: ")
class_id = input("Enter class ID (check from classes table): ")

cursor.execute("""
    INSERT INTO students (name, roll_number, class_id)
    VALUES (?, ?, ?)
""", (name, roll_number, class_id))

conn.commit()
print("✅ Student added successfully!")
conn.close()
