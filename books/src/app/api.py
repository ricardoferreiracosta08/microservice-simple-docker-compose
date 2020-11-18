import json

from flask import request

from . import create_app, database
from .models import Books

app = create_app()

@app.route('/', methods=['GET'])
def fetch():
    books = database.get_all(Books)
    all_books = []
    for book in books:
        new_book = {
            "id": book.id,
            "name": book.name,
            "price": book.price,
        }

        all_books.append(new_book)
    return json.dumps(all_books), 200


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    name = data['name']
    price = data['price']

    database.add_instance(Books, name=name, price=price)
    return json.dumps("Added"), 200


@app.route('/remove/<book_id>', methods=['DELETE'])
def remove(book_id):
    database.delete_instance(Books, id=book_id)
    return json.dumps("Deleted"), 200


@app.route('/edit/<book_id>', methods=['PATCH'])
def edit(book_id):
    data = request.get_json()
    new_price = data['price']
    database.edit_instance(Books, id=book_id, price=new_price)
    return json.dumps("Edited"), 200
