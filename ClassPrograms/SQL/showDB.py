import sqlite3

conn = sqlite3.connect('sample.db')

j = conn.execute(".tables")
print(j)
conn.close()