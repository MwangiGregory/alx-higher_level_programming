#!/usr/bin/python3
# A script that lists all states from the database hbtn_0e_0_usa
import MySQLdb
import sys

username, password, db_name = sys.argv[1:]
db = MySQLdb.connect(host='127.0.0.1', user=username,
                     passwd=password, db=db_name, port=3306)
cur = db.cursor()
cur.execute('SELECT * FROM states ORDER BY states.id ASC')
rows = cur.fetchall()

for row in rows:
    print(row)
