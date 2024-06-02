from flask import Flask, request, jsonify
import socket


app = Flask(__name__)
@app.route('/hello')
def hello():
    return 'Hi'



