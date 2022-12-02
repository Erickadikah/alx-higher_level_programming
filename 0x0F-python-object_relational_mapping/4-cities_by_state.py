#!/usr/bin/python3
import sys
import MySQLdb


db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],db=sys.argv[3], port=3306)

if __name__ == "__main__":
    cur = db.cursor()
    cur.execute("SELECT `cities`.`id`,`cities`.`name`, `states`.`name`\
            FROM `cities` INNER JOIN `states` ON `cities`.`state_id` = `states`.`id`\
            ORDER BY `cities`.`id`")
    [print(city) for city in cur.fetchall()]

cur.close()
db.close()
