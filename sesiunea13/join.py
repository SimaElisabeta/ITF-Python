import sqlite3
from pprint import pprint

con = sqlite3.connect("students.db")
cursor = con.cursor()

SQL_query = "SELECT * FROM Students s JOIN Grades g ON s.ID=g.student_id WHERE s.name=?"
cursor.execute(SQL_query, ("Eva",))
pprint(cursor.fetchall())

print('*' * 50)
# Numele, materia si nota pentru studentul Adam

SQL_query = "SELECT s.name, g.topic, g.grade FROM Students s JOIN Grades g ON s.ID=g.student_id WHERE s.name=?"
cursor.execute(SQL_query, ("Eva",))
pprint(cursor.fetchall())
