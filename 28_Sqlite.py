# Sqlite3 module in python

# Work with sqlite3 database in python

import sqlite3

db = sqlite3.connect("test.db")                                             # Connect and create database

db.execute("DROP TABLE IF EXISTS test")                                     # Delete table if name is "test"

db.execute("CREATE TABLE test(name text, age int)")                         # Create table and columns

db.execute("INSERT INTO test (name, age) VALUES (?,?)",("Ahmad", 21))       # Insert rows in table columns
db.execute("INSERT INTO test (name, age) VALUES (?,?)",("Ali", 17))
db.execute("INSERT INTO test (name, age) VALUES (?,?)",("Ghasem", 26))
db.execute("INSERT INTO test (name, age) VALUES (?,?)",("Reza", 23))

db.commit()

cursor = db.execute("SELECT * FROM test")                                   # Selecet all data in table 

for row in cursor:                                                          # Print all data in table
    print(row)