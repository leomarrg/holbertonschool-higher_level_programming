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
    user_input = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=name,
        port=3306
    )
    if (db):
        cur = db.cursor()

        cur.execute("SELECT cities.name \
                    FROM cities INNER JOIN states ON cities.state_id \
                    = states.id WHERE states.name = %s;", (user_input,))

        rows = cur.fetchall()
        num_rows = len(rows)
        for i, row in enumerate(rows):
            print(row[0], end='')
            if i < num_rows - 1:
                print(', ', end='')
            else:
                print("")
    else:
        print("Connection failed...")
