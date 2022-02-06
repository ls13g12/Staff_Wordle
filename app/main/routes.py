from app.main import bp
from flask import Flask, render_template, jsonify, request

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')

@bp.route('/get_word', methods = ["GET","POST"])
def get_word():
    return jsonify({'data': "water"})