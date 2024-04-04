#!/usr/bin/python3
"""
a script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""


from sys import argv
import MySQLdb

if __name__ == '__main__':
    mysql_username = argv[1]
    mysql_pwd = argv[2]
    db_name = argv[3]
    state_name_searched = argv[4]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_pwd,
        db=db_name
        )
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cur.execute(query, (state_name_searched,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
