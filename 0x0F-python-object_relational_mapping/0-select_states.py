#!/usr/bin/python3

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
