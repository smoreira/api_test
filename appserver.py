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


@app.route('/balance', methods=['GET'])
def balance():
    response = {}
    if request.method != 'GET':
        response['status'] = False
        response['message'] = 'Invalid request'

    return jsonify(response)


@app.route('/event', methods=['POST'])
def balance():
    response = {}
    if request.method != 'POST':
        response['status'] = False
        response['message'] = 'Invalid request'

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False, threaded=False)