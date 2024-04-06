#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa
"""


from sys import argv
import MySQLdb

if __name__ == '__main__':
    mysql_username = argv[1]
    mysql_pwd = argv[2]
    db_name = argv[3]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_pwd,
        db=db_name
        )
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name AS city_name, \
        states.name AS state_name \
        FROM cities \
        JOIN states ON cities.state_id = states.id \
        ORDER BY cities.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
