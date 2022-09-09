#!/usr/bin/python3
"""
This script lists all the states from
database hbtn_0e_0_usa. The script takes 3 arguments:
mysql username, mysql password and database name
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    username, password, database = sys.argv[1:]
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
