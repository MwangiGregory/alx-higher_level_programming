#!/usr/bin/python3
"""This script lists all cities from the database hbtn_0e_4_usa.
The script takes 3 arguments: mysql username, mysql password
and database name"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    username, password, database = sys.argv[1:]
    db = MySQLdb.connect(
            user=username,
            passwd=password,
            db=database,
            host='localhost',
            port=3306)
    cur = db.cursor()
    sql_query = """
            SELECT cities.`id`, cities.`name`, states.`name`
            FROM `cities` INNER JOIN `states`
            ON cities.`state_id` = states.`id`
            ORDER BY cities.`id` ASC;"""
    cur.execute(sql_query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
