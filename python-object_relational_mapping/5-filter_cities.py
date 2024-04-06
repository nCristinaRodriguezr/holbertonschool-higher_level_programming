#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
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
    query = "SELECT cities.name \
    FROM cities \
    JOIN states ON cities.state_id = states.id \
    WHERE states.name = %s \
    ORDER BY cities.id ASC"
    cur.execute(query, (state_name_searched,))
    rows = cur.fetchall()
    city_names = ', '.join(city[0] for city in rows)
    print(city_names)
    cur.close()
    db.close()
