import json

from flask import request

from . import create_app, database
from .models import Readers

app = create_app()

@app.route('/', methods=['GET'])
def fetch():
    readers = database.get_all(Readers)
    all_readers = []
    for reader in readers:
        new_reader = {
            "id": reader.id,
            "name": reader.name,
        }

        all_readers.append(new_reader)
    return json.dumps(all_readers), 200


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    name = data['name']

    database.add_instance(Readers, name=name)
    return json.dumps("Added"), 200


@app.route('/remove/<reader_id>', methods=['DELETE'])
def remove(reader_id):
    database.delete_instance(Readers, id=reader_id)
    return json.dumps("Deleted"), 200


@app.route('/edit/<reader_id>', methods=['PATCH'])
def edit(reader_id):
    data = request.get_json()
    database.edit_instance(Readers, id=reader_id)
    return json.dumps("Edited"), 200
