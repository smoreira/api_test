import os
import numpy as np
import urllib.request

from flask import Flask, flash, request, redirect, url_for
from flask import send_from_directory
from flask import jsonify
from flask import render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['JSON_AS_ASCII'] = False


@app.route('/reset', methods=['GET', 'POST'])
def base():
    return "OK"


@app.route('/balance', methods=['GET'])
def balance():
    account_id = request.args.get('account_id')
    response = {}
    if request.method != 'GET':
        response['status'] = False
        response['message'] = 'Invalid request'
    else:
        if account_id == "100":
            return '20', 200
        else:
            return '0', 404

    return jsonify(response)


@app.route('/event', methods=['POST'])
def event():
    response = {}
    if request.method != 'POST':
        response['status'] = False
        response['message'] = 'Invalid request'
    else:
        response['status'] = '200'
        response['message'] = 'deu certo'

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False, threaded=False)
