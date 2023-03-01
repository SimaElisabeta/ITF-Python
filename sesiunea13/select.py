import sqlite3
from pprint import pprint

con = sqlite3.connect("students.db")
cursor = con.cursor()

print('*' * 50)
cursor.execute("SELECT * FROM Students")
# pprint(cursor.fetchall())
pprint(cursor.fetchone())
pprint(cursor.fetchone())

print('*' * 50)
cursor.execute("SELECT * FROM Grades")
pprint(cursor.fetchmany(3))
pprint(cursor.fetchone())

print('*' * 50)
cursor.execute("SELECT topic, grade FROM Grades")
pprint(cursor.fetchall())

print('*' * 50)
cursor.execute("SELECT * FROM Grades WHERE topic=?", ('WEB Dev',))
pprint(cursor.fetchall())

print('*' * 50)
# Numele si email-ul tuturor studentilor cu varsta < 26
cursor.execute("SELECT name, email FROM Students WHERE age<26")
pprint(cursor.fetchall())
