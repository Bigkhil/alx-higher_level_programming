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
                   WHERE `states`.`name` = {}\
                   ORDER BY `cities`.`id`".format(sys.argv[4]))
    rows = cursor.fetchall()
    for i in len(rows) - 2:
        print(rows[i] + ',', end="")
    print(rows[len[rows] - 1])
    conn.close()


if __name__ == "__main__":
    main()
