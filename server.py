# coding: utf-8

import json
from flask import Flask, render_template, make_response, request, Response, jsonify
from jinja2 import Environment, PackageLoader
from atlas_db import AtlasDB

from flask_cors import CORS
# pip3 install -U flask-cors

from bson.json_util import dumps

db = AtlasDB('localhost:27017', 'agenda', 'contatos')

app = Flask(__name__)
CORS(app)


# ****************************************************** HOME ******************************************************

@app.route('/user/<string:id>/contatos', methods=['GET'])
def home(id):
    res = db.getAll(id)
    lista = []
    for line in res:
        contact = {
            '_id': str(line['_id']),
            'name': line['name'],
            'tel': line['tel'],
            'email': line['email'],
            'cep': line['cep'],
            'city': line['city'],
            'state': line['state'],
            'andress': line['andress'],
            'description': line['description'],
            'user_id': line['user_id']
        }
        lista.append(contact)
    return jsonify(lista)


# ****************************************************** INSERE ******************************************************

@app.route('/user/<string:user_id>/insere', methods=['POST'])
def insereContato(user_id):
    try:
        dados = json.loads(request.data)
        contact = {
            'name': dados['name'],
            'tel': dados['tel'],
            'email': dados['email'],
            'cep': dados['cep'],
            'city': dados['city'],
            'state': dados['state'],
            'andress': dados['andress'],
            'description': dados['description'],
            'user_id': dados['user_id']
        }
        res = db.insertItem(contact)
        return jsonify({'status': res})
    except:
        return jsonify({'status': False})


# ****************************************************** DELETE ******************************************************

@app.route('/user/<string:user_id>/delete/<string:contact_id>', methods=['DELETE'])
def deletaContato(user_id, contact_id):
    #request.data.get('text', '')
    try:
        res = db.deleteItem(contact_id)
        return jsonify({'status': res})
    except:
        return jsonify({'status': False})


# ****************************************************** UPDATE ******************************************************

@app.route('/user/<string:user_id>/update/<string:contact_id>', methods=['PUT'])
def updateContato(user_id, contact_id):
    try:
        dados = json.loads(request.data)
        print(dados)
        contact = {
            'name': dados['name'],
            'tel': dados['tel'],
            'email': dados['email'],
            'cep': dados['cep'],
            'city': dados['city'],
            'state': dados['state'],
            'andress': dados['andress'],
            'description': dados['description'],
            'user_id': dados['user_id']
        }
        res = db.updateItem(dados['_id'], contact)
        return jsonify({'status': res})
    except ValueError:
        return jsonify({'status': False})


# ****************************************************** MAIN ******************************************************

if __name__ == "__main__":
    app.secret_key = 'm;4slF=Y6]Afb/.p9Xd7iO8(V0yU~R"'
    app.run(host='0.0.0.0', port=8989, threaded=True, debug=True)
