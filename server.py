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

@app.route('/user/<string:id>/contatos', methods=['GET'])
def home(id):
    res = db.getAll(id)
    lista = []
    for line in res:
        contact = {
            'id': str(line['_id']),
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


@app.route('/user/<string:user_id>/insere', methods=['POST'])
def insereContato(user_id):
    try:
        dados = json.loads(request.data)
        res = db.insertItem(dados)
        return jsonify({'status': res})
    except:
        return jsonify({'status': False})


@app.route('/user/<string:user_id>/delete/<string:contact_id>', methods=['DELETE'])
def deletaContato(user_id, contact_id):
    #request.data.get('text', '')
    try:
        res = db.deleteItem(contact_id)
        return jsonify({'status': res})
    except:
        return jsonify({'status': False})

@app.route('/user/<string:user_id>/update/<string:contact_id>', methods=['PUT'])
def updateContato(user_id, contact_id):
    dados = json.loads(request.data)
    print(dados['name'])
    print('\n***** ********\n')
    return jsonify({'msg': True})


'''# Retorna uma página com 30 itens.
@app.route('/alimentos', methods=['GET'])
def pagina():
    # http://localhost:8989/alimentos?pag=1&campo=kcal&sort=-1
    pag = request.args.get('pag')
    campo = request.args.get('campo')
    sort = request.args.get('sort')
    print(pag, campo, sort)
    
    res = db.getPag(pag, campo, sort)

    if res['erro'] == 404:
        res = jsonify(res)
        res.status_code = 404
        return res

    lista = []
    for line in res['msg']:
        lista.append(line)

    res = jsonify(lista)
    res.status_code = 200
    return res


# Retorna todos os alimentos que começam com a string passada(nome)
@app.route('/alimento/<string:nome>', methods=['GET'])
def alimento_nome(nome):
    res = db.getPorNome(nome)
    lista = []
    
    for line in res:
        lista.append(line)
    
    res = jsonify(lista)
    res.status_code = 200
    return res'''

if __name__ == "__main__":
    app.secret_key = 'm;4slF=Y6]Afb/.p9Xd7iO8(V0yU~R"'
    app.run(host='0.0.0.0', port=8989, threaded=True, debug=True)
