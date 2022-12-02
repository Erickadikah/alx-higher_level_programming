#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa
take 3 arguments<mysql username>
                <mysql password>
                <database name>

"""
import sys
import MySQLdb

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],db=sys.argv[3], port=3306)

if __name__ == "__main__":
    cur = db.cursor()
    cur.execute("USE `hbtn_0e_0_usa`")
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall()]

cur.close()
db.close()
