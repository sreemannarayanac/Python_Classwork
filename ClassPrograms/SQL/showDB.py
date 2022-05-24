import sqlite3

conn = sqlite3.connect('sample.py')

j = conn.execute("SHOW TABLES;")
conn.flush()