import sqlite3
from pprint import pprint

con = sqlite3.connect("students.db")
cursor = con.cursor()

SQL_query = "DELETE FROM Grades WHERE topic=:topic AND student_id=:id"

values = {
    'id': 1,
    'topic': 'WEB Dev'
}

cursor.execute(SQL_query, values)
cursor.execute("SELECT * FROM Grades")
pprint(cursor.fetchall())

con.commit()
