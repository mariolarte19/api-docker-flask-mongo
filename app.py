from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, ObjectId
from os import environ

app = Flask(__name__)
app.config["MONGO_URI"] = environ.get("MONGO_URI")
mongo = PyMongo(app)
db = mongo.db


@app.route('/api/book/<book_id>', methods=['GET'])
def getBook(book_id):
    _book = db.book.find_one({"_id": ObjectId(book_id)})
    item = {
        'id': str(_book['_id']),
        'book': _book['book']
    }

    return jsonify(data=item), 200


@app.route('/api/book', methods=['GET'])
def getBooks():
    _books = db.book.find()
    item = {}
    data = []
    for book in _books:
        item = {
            'id': str(book['_id']),
            'book': book['book']
        }
        data.append(item)

    return jsonify(data=data), 200


@app.route('/api/book', methods=['POST'])
def createbook():
    data = request.get_json(force=True)
    item = {
        'book': data['book']
    }
    db.book.insert_one(item)

    return jsonify(data=data), 201


@app.route('/api/book/<book_id>', methods=['PATCH'])
def updatebook(book_id):
    data = request.get_json(force=True)
    db.book.update_one({"_id": ObjectId(book_id)}, {"$set": data})

    return jsonify(data=data), 204


@app.route('/api/book/<book_id>', methods=['DELETE'])
def deletebook(book_id):
    db.book.delete_one({"_id": ObjectId(book_id)})

    return jsonify(), 204


if __name__ == "__main__":
    ENVIRONMENT_DEBUG = environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = environ.get("APP_PORT", 5000)
    app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)