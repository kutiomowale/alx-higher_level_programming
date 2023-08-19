#!/usr/bin/python3
"""All cities by state

This module takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa

The MySQLdb module is used

The mysql username, password, the database name and the state name to display
its cities are passed as command line arguments

"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                           passwd=mysql_password,
                           db=database_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT cities.name FROM cities WHERE state_id = (
                SELECT states.id FROM states WHERE states.name = %s)
                ORDER BY cities.id ASC""", (state_name, ))
    query_rows = cur.fetchall()
    for row in query_rows[0:-1]:
        print(row[0], end=', ')
    print(query_rows[-1][0])
    cur.close()
    conn.close()
