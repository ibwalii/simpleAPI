import sqlite3

conn = sqlite3.connect("books.sqlite")

cursor = conn.cursor()

sqlQuery = """ CREATE TABLE books (
    id integer PRIMARY KEY,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL 
)
"""
cursor.execute(sqlQuery)