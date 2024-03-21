#!/usr/bin/python3
"""
Lists states that user inputs rom database hbtn_0e_0_usa
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

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE \
                name = '{}' ORDER BY id;".format(user_input))

    rows = cur.fetchall()
    for row in rows:
        print(row)
