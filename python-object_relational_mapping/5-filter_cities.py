#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa

Your script should take 4 arguments: mysql username, mysql password, database
name and state name (SQL injection free!)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
The results must be displayed as they are in the example below
Your code should not be executed when imported
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cursor = connection.cursor()
    query = "SELECT cities.name FROM cities\
            JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s ORDER BY cities.id"
    cursor.execute(query, (argv[4],))

    records = cursor.fetchall()

    print(", ".join([record[0] for record in records]))

    cursor.close()
    connection.close()
