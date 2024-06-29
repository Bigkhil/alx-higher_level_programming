#!/usr/bin/python3
'''this script should list all states in the database that start with N'''
import MySQLdb
import sys


def main():
    '''main fucntion to execute when using the script'''
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT `cities`.`id`, `cities`.`name`, `states`.`name`\
                   FROM `cities` JOIN `states` ON `states`.`state_id` = `cities`.`id`\
                   ORDER BY `cities`.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()


if __name__ == "__main__":
    main()
