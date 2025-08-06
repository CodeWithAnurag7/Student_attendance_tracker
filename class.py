import sqlite3

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

class_name = input("Enter class name ")

cursor.execute("INSERT INTO classes (name) VALUES (?)", (class_name,))
conn.commit()

print("✅ Class added successfully!")
conn.close()
