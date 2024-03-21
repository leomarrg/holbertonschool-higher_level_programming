#!/usr/bin/python3
import sys
import MySQLdb


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username,
                        passwd=password, db=name, port = 3306)
    #cursos object
    #execute all queries you need
    cur = db.cursor()

    #Use all SQL you like
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

