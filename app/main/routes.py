from app.main import bp
from flask import Flask, render_template, jsonify, request
from flask_login import login_required

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    return render_template('index.html')

@bp.route('/get_word', methods = ["GET","POST"])
def get_word():
    return jsonify({'data': "water"})