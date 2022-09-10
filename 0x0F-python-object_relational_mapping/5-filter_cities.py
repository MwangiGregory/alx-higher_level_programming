#!/usr/bin/python3
"""This script takes in the name of a state as an argument
and lists all cities of that state using the database hbtn_0e_4_usa"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    username, password, database, state_name = sys.argv[1:]
    db = MySQLdb.connect(
            user=username,
            passwd=password,
            db=database,
            host='localhost',
            port=3306)
    cur = db.cursor()
    sql_query = """
            SELECT cities.`name` FROM `cities`
            INNER JOIN `states`
            ON cities.`state_id` = states.`id`
            WHERE states.`name` = %s
            ORDER BY cities.`id` ASC;"""
    cur.execute(sql_query, (state_name,))
    rows = cur.fetchall()
    result = ''
    for row in rows:
        result += row[0]
        if rows.index(row) != (len(rows) - 1):
            result += ', '
    print(result)
