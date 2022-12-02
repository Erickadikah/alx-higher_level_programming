#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_4_usa
whose name matches that supplied as argument.

"""
import sys
from sys import argv
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd=sys.argv[2], port=3306, db="hbtn_0e_4_usa")

if __name__ == "__main__":
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE {:s} ORDER BY id ASC", argv[4],)
    rows = cur.fetchall()
    for cities in rows:
            print(cities)
cur.close()
db.close()
