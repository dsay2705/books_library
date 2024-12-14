from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id": 1,
    "author": "Jon",
    "title": "First Book"}
]

@app.route("/test")
def test():
    return "Test is working"

@app.route("/books", methods = ['GET'])
def get_books():

    author = request.args.get('author')
    # MARK: // rewrite to function
    for book in books:
        if book.get('author') == author:
            return jsonify([book.get('author'), book.get('title')], 200)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)