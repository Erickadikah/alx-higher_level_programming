#!/usr/bin/python3
import sys
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd=sys.argv[2], port=3306, db = "hbtn_0e_0_usa")

if __name__ == "__main__":
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1][0] == "N":
            print(row)

cur.close()
db.close()
