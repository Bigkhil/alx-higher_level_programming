#!/usr/bin/python3
'''this script should list all cities related to a specific state'''
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
    print(", ".join([row[0] for row in rows]))
    conn.close()


if __name__ == "__main__":
    main()
