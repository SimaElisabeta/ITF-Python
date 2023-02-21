import sqlite3

con = sqlite3.connect("students.db")
cursor = con.cursor()
cursor.executescript("""
CREATE TABLE if not exists Students (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    age INTEGER CHECK (age > 18)
);

CREATE TABLE if not exists Grades (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT,
    grade INTEGER NOT NULL CHECK (0 < grade AND grade < 10),
    student_id INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Students(ID)
);
""")

cursor.execute("SELECT * FROM Students")
print(cursor.fetchall())
