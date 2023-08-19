#!/usr/bin/python3
"""Cities by states

This module lists all cities from the database hbtn_0e_4_usa

The MySQLdb module is used

The mysql username, password and the database name
arw passed as command line arguments

"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                           passwd=mysql_password,
                           db=database_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities, states
                WHERE cities.state_id = states.id
                ORDER BY cities.id""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
