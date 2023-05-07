from flask import Flask, request, jsonify

app = Flask(__name__)

book_list = [{
    "id": 0,
    "author": "Chinua Achebe",
    "language": "English",
    "title": "Things fall apart"
    },
    {
    "id": 1,
    "author": "Chinua Achebe 2",
    "language": "English",
    "title": "Things fall apart 2"
    }
]

@app.route('/books', methods = ['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(book_list):
            return jsonify(book_list)
        else:
            'Nothing Found', 404
    
    if request.method == 'POST':
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        new_id = book_list[-1]['id']+1

        new_obj = {
            "id": new_id,
            "author": new_author,
            "language": new_lang,
            "title": new_title
        }

        book_list.append(new_obj)
        return jsonify(book_list)

@app.route('/')
def index():
    return '<h1>Hello </h1>'

@app.route('/<name>')
def print_name(name):
    return '<h1>Hi, {}</h1>'.format(name)

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
