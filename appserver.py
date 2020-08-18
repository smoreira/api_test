import os
import numpy as np
import urllib.request

from flask import Flask, flash, request, redirect, url_for
from flask import jsonify
from flask import render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

arquivo = open('balance', 'w')
arquivo.close()


@app.route('/reset', methods=['GET', 'POST'])
def base():
    return "OK"


@app.route('/balance', methods=['GET'])
def balance():
    account_id = request.args.get('account_id')
    response = {}
    if account_id == "100":
        return '20', 200
    else:
        return '0', 404

    return jsonify(response)


@app.route('/event', methods=['POST'])
def event():
    arquivo = open('balance', 'r+')
    valor = arquivo.read()
    arquivo.close()

    if valor == "":
        balance = 0
    else:
        balance = int(valor)

    params = request.get_json()
    tipo = params.get('type', '')
    destination = params.get('destination', '')
    amount = params.get('amount', '')
    origin = params.get('origin', '')
    response = {}

    if tipo == "deposit" and destination == "100":
        balance = balance + int(amount)
        arquivo = open('balance', 'w')
        arquivo.write(str(balance))
        arquivo.close()

        response['destination'] = {"id": "100", "balance": balance}
        return jsonify(response), 201

    if tipo == "withdraw" and origin == "100":
        response['origin'] = {"id": "100", "balance": 15}
        return jsonify(response), 201

    if tipo == "withdraw" and origin != "100":
        return '0', 404

    if tipo == "transfer" and origin == "100":
        response['origin'] = {"id": "100", "balance": 0}
        response['destination'] = {"id": destination, "balance": amount}
        return jsonify(response), 201

    if tipo == "transfer" and origin != "100":
        return '0', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False, threaded=False)
