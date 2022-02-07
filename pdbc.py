# Day 7 Assignment - Python Database Connection Project which updates any one value in the table and select all the table data and print it.

#pip install mysql-Connector
import mysql.connector as sqlcon

db = sqlcon.connect(host = '127.0.0.1', user = 'root', password = 'mysqlDubey@209', database = 'essentials')

cur = db.cursor()

cur.execute("update student set mark = 94 where sname = 'Varun'")
cur.execute('select * from student')

for i in cur:
    print(i)

cur.close()

db.commit()