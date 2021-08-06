#!/usr/bin/python3
""" Script takes an argument and sql injection"""
import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        host="localhost",
        port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM cities ORDER BY cities.id ASC")
    for i in cursor.fetchall():
        print(i)
    cursor.close()
    db.cursor()
