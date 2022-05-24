import sqlite3

conn = sqlite3.connect('sample.db')

conn.execute('''CREATE TABLE COMPANY
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL);''')

print('Connection Successful and made a sample table of company')
conn.close()