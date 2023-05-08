from flask import Flask, request, jsonify
import json
import pymysql

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = pymysql.connect( host='localhost',
                                user='root',
                                password='root',
                                db='simpleCRUD')
    except pymysql.error as e:
        print(e)
    return conn


@app.route('/books', methods = ['GET', 'POST'])
def books():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM books")
        books = [
            dict(id = row[0], author = row[1], language = row[2], title = row[3])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)
    
    if request.method == 'POST':
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        sqlQuery = """ INSERT INTO books(author, language, title)
                        VALUES(%s, %s, %s)"""
        cursor.execute(sqlQuery, (new_author, new_lang, new_title))
        conn.commit()
        return f"Book with ID: { cursor.lastrowid} added successfully"

@app.route('/books/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        sqlQuery = """ SELECT * FROM books where ID =%s """
        cursor.execute(sqlQuery,(id,))
        row = cursor.fetchall()
        for book in row:
            book = book
        if book is not None:
            return jsonify(book), 200
        else:
            return "something went wrong", 404
        
    
    if request.method == 'PUT':
        sqlQuery = """ UPDATE books 
                        set author= %s, 
                        language= %s,  
                        title= %s 
                        where id= %s """
        title = request.form['title']
        author = request.form['author']
        language = request.form['language']

        updated_book = {
            "id": id,
            "author": author,
            "language": language,
            "title": title
        }
        
        cursor.execute(sqlQuery, (author, language, title, id))
        conn.commit()
        
        return jsonify(updated_book)

    if request.method == 'DELETE':
        sqlQuery = """ DELETE FROM books where id=%s """
        cursor.execute(sqlQuery, (id,))
        conn.commit()
        return f" DELETED Book with ID: {id} successfully", 200

    


@app.route('/')
def index():
    return '<h1>Hello </h1>'

@app.route('/<name>')
def print_name(name):
    return '<h1>Hi, {}</h1>'.format(name)

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
