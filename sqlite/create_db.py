import sqlite3
conn=sqlite3.connect("site.db")
cursor=conn.cursor() #it means now we are allowing to send command on db

cursor.execute('''
CREATE TABLE student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL   
)
''')
conn.commit() #to save changes permenantly
conn.close()
