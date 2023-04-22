#!/usr/bin/python3
"""This script takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument."""

import sys
import MySQLdb

if __name__ == "__main__":
    username, password, db_name, state_name = sys.argv[1:]
    db = MySQLdb.connect(
        host='localhost', port=3306,
        user=username, passwd=password, database=db_name
    )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states \
         WHERE states.name LIKE '{}' \
         ORDER BY states.id ASC"
        .format(state_name))

    for state in cur.fetchall():
        print(state)
