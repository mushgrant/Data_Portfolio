import sqlite3
conn = sqlite3.connect('factbook.db')
c = conn.cursor()
c.execute("SELECT * FROM facts ORDER BY population DESC limit 10;")
print(c.fetchall())