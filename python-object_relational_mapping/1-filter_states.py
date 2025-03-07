#!/usr/bin/python3
'''
This module  lists all states starting with N from the database hbtn_0e_0_usa
'''
import MySQLdb
import sys

if __name__ == "__main__":

    if len(sys.argv) != 4:
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT DISTINCT * FROM states "
                   "WHERE name LIKE 'N%' "
                   "ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
