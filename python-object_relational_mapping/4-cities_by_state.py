#!/usr/bin/python3
"""
Lists cities from database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=name,
        port=3306
    )
    if (db):
        cur = db.cursor()

        cur.execute("SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY id")
        rows = cur.fetchall()
        for row in rows:
            print(row)

        rows = cur.fetchall()
        for row in rows:
            print(row)
    else:
        print("Connection failed...")