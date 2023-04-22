#!/usr/bin/python3
"""This script takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""

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
        """
        SELECT cities.name FROM cities
        WHERE cities.state_id = (
        SELECT states.id
        FROM states
        WHERE states.name = %s)
        ORDER BY cities.id ASC""", (state_name,)
    )

    cities = cur.fetchall()
    for index, city in enumerate(cities):
        print(city[0], end='')
        if index != len(cities) - 1:
            print(', ', end='')
    print()
