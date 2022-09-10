#!/usr/bin/python3
"""
This script takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    username, password, database, state_name = sys.argv[1:]
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database)
    cur = db.cursor()
    sql_query = """
            SELECT * FROM `states`
            WHERE BINARY `name` = %s 
            ORDER BY `id` ASC
            """
    print(state_name)
    cur.execute(sql_query, (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close
