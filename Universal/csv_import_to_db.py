import sqlite3
import csv

connection = sqlite3.connect('SQLite_Python.db')
cursor = connection.cursor()

with open('czasy.csv', 'r', newline='', encoding='utf-8') as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO SqliteDb_German_Time VALUES (?,?)", row.split(","))
        connection.commit()
        no_records += 1
connection.close()
print("\n{} Record Transferred".format(no_records))
