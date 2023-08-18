#!/usr/bin/python3
"""Filter states by user input

This module displays all the staes with a name matching user input
from the states table
in a particular mysql database

The MySQLdb module is used

The mysql username, password and the database name and the state name to match
are passed as command line arguments

"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                           passwd=mysql_password,
                           db=database_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states
                WHERE name = % s ORDER BY id ASC""", (state_name_searched, ))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
