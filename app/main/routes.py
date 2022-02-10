from app.models import User, Word, UserWordLink
from app.main import bp
from app import db
from flask import Flask, render_template, jsonify, request
from flask_login import login_required
from datetime import date, timedelta
from sqlalchemy import func
from app.main.words import get_new_word

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    return render_template('index.html')

@bp.route('/get_word', methods = ["GET","POST"])
def get_word():

    new_word = get_new_word()
    print(new_word)
    
    word = Word(name=new_word)
    
    if not Word.query.filter_by(name=new_word).first():
        db.session.add(word)
        db.session.commit()

    return jsonify({'data': new_word})

@bp.route('/leaderboard')
@login_required
def leaderboard():
    
    return render_template('leaderboard.html')

@bp.route('/leaderboard_data')
@login_required
def leaderboard_data():

    days_span = 3

    starting_date = date.today() - timedelta(days = days_span)
    tomorrows_date = date.today() + timedelta(days = 1)

    #query all users who have completed the word, sorted by number of guesses ascending
    today_word_users = UserWordLink.query.filter(UserWordLink.date >= starting_date, UserWordLink.date < tomorrows_date
    ).join(User).join(Word).order_by(UserWordLink.guesses).all()

    return jsonify({'data' : [(today_word_user.user.initials, today_word_user.guesses) for today_word_user in today_word_users]})

@bp.route('/update_database', methods = ['GET', 'POST'])
@login_required
def update_leaderboard():

    #new word currently input by hard coding 
    new_word = 'paper'
    guesses = 5

    #queries word or adds word to db
    word = Word.query.filter_by(name=new_word).first()
    if not word:
        word = Word(name=new_word)
        db.session.add(word)
        db.session.commit()

    #query user in db
    user = User.query.filter_by(initials='ABC').first()

    #query the user_word or adds to the db
    user_word1 = UserWordLink(user_id=user.id, word_id=word.id, guesses=guesses)
    if not UserWordLink.query.filter_by(user=user, word=word).first():
        db.session.add(user_word1)
        db.session.commit()
    
