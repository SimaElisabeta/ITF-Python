import sqlite3

con = sqlite3.connect("students.db")
cursor = con.cursor()

cursor.execute("INSERT INTO STUDENTS (name, email, age) VALUES ('Adam', 'adam@g.com', 28)")
cursor.execute("INSERT INTO STUDENTS (name, email, age) VALUES ('Eva', 'eva@g.com', 25)")

cursor.execute("SELECT * FROM Students")
print(cursor.fetchall())

grades_values = [
    ('WEB Dev', 8, 1),
    ('DB Dev', 9, 1),
    ('DB Dev', 6, 2),
    ('FRONTEND Dev', 9, 2),
    ('WEB Dev', 9, 2),
    ('WEB Dev', 8, 2),
    ('WEB Dev', 7, 1)
]

SQL_query = "INSERT INTO GRADES (topic, grade, student_id) VALUES (?,?,?)"
cursor.executemany(SQL_query, grades_values)
cursor.execute("SELECT * FROM Grades")
print(cursor.fetchall())
con.commit()
