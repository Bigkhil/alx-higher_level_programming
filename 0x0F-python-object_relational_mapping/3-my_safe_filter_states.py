#!/usr/bin/python3
'''this script should list all states in the database that start with N'''
import MySQLdb
import sys


def main():
    '''main fucntion to execute when using the script'''
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cursor = conn.cursor()
    param = sys.arg[4]
    cursor.execute("SELECT * from states WHERE `name` = %s;",
                   (param, ))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()


if __name__ == "__main__":
    main()
