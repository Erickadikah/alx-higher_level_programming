#!/usr/bin/python3
"""
    a script that lists all states with a name starting with N(upper)
    from datbase hbtn_0e_0_usa:
"""
import sys
import MySQLdb

db = MySQLdb.connect(user=sys.argv[0], passwd=sys.argv[1],db=sys.argv[2], port=3306)

if __name__ == "__main_":
    cur == db.cursor()
    cur.execute("USE `hbtn_0e_0_usa`")
    cur.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in cur.fetchall() if state [1][0] == ["N"]]


cur.close()
db.close()
