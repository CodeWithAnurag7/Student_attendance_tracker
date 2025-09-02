import sqlite3
import os

# Define the full path to the database
DB_FOLDER = "/Users/anuragyadav/Documents/Projects/Student_attendacne_tracker/database"
DB_NAME = os.path.join(DB_FOLDER, "students.db")

# Ensure the directory exists
os.makedirs(DB_FOLDER, exist_ok=True)

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

sql_script_path = os.path.join(os.path.dirname(__file__), "setup.sql")
with open(sql_script_path, "r") as f:
    sql_script = f.read()

cursor.executescript(sql_script)
conn.commit()
conn.close()

print(f"Database '{DB_NAME}' successfully created with tables!")