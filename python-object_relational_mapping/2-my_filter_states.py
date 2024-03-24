#!/usr/bin/python3

"""Write a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.

Your script should take 4 arguments: mysql username, mysql password, database
name and state name searched (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
You must use format to create the SQL query with the user input
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])

    cursor = connection.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id"
            .format(argv[4]))

    records = cursor.fetchall()
    for record in records:
        print(record)

    cursor.close()
    connection.close()
