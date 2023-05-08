import pymysql

# Establish a connection to the database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='simpleCRUD'
)

cursor = conn.cursor()


sqlQuery = """ CREATE TABLE books (
    id integer PRIMARY KEY AUTO_INCREMENT,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL 
)
"""
cursor.execute(sqlQuery)
conn.close()