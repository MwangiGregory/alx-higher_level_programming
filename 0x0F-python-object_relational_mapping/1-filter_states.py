#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database
hbtn_oe_0_usa. The script takes three arguments:
mysql username, mysql password and database name
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    username, password, database = sys.argv[1:]
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute("
        SELECT * FROM `states` WHERE `name` LIKE 'N%' ORDER BY `id` ASC                 ")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
