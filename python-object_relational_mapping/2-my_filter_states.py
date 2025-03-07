#!/usr/bin/python3
# Displays all values in the states table of the database hbtn_0e_0_usa
# whose name matches that supplied as argument.
# Usage: ./2-my_filter_states.py <mysql username> \
#                                <mysql password> \
#                                <database name> \
#                                <state name searched>

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    # Query to select states where name matches the argument (case-sensitive)
    query = "SELECT * FROM `states` WHERE BINARY `name` = '{}' ORDER BY id ASC".format(sys.argv[4])

    # Execute the query
    c.execute(query)

    # Fetch all results and print them
    states = c.fetchall()
    for state in states:
        print(state)

    # Close cursor and database connection
    c.close()
    db.close()
