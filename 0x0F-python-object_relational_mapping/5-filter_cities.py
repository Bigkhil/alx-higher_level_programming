#!/usr/bin/python3
'''this script should list all states in the database that start with N'''
import MySQLdb
import sys


def main():
    '''main fucntion to execute when using the script'''
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT `cities`.`name`\
                   FROM `cities`\
                   JOIN `states` ON `cities`.`state_id` = `states`.`id`\
                   WHERE `states`.`name` = {}".format(sys.argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()


if __name__ == "__main__":
    main()
