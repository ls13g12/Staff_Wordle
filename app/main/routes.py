from urllib import response
from app.models import User, Word, UserWordLink
from app.main import bp
from app import db
from flask import Flask, render_template, jsonify, request, json
from flask_login import login_required, current_user
from datetime import date, timedelta
from app.main.words import get_new_word
import pendulum

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


@bp.route('/today_leaderboard_data')
@login_required
def today_leaderboard_data():
    starting_date = date.today()
    tomorrows_date = date.today() + timedelta(days = 1)

    #query all users who have completed the word, sorted by number of guesses ascending
    today_word_users = UserWordLink.query.filter(UserWordLink.date >= starting_date, UserWordLink.date < tomorrows_date
    ).join(User).join(Word).order_by(UserWordLink.guesses).all()

    return jsonify({'initials' : [today_word_user.user.initials for today_word_user in today_word_users],
                    'guesses': [today_word_user.guesses for today_word_user in today_word_users]})


@bp.route('/week_leaderboard_data')
@login_required
def week_leaderboard_data():
    today = pendulum.now()
    starting_date = today.start_of('week')
    tomorrows_date = date.today() + timedelta(days = 1)


    #query all users who have completed the word, sorted by number of guesses ascending
    today_word_users = UserWordLink.query.filter(UserWordLink.date >= starting_date, UserWordLink.date < tomorrows_date
    ).join(User).join(Word).order_by(UserWordLink.guesses).all()

    return jsonify({'initials' : [today_word_user.user.initials for today_word_user in today_word_users],
                    'guesses': [today_word_user.guesses for today_word_user in today_word_users]})


@bp.route('/month_leaderboard_data')
@login_required
def month_leaderboard_data():
    today = pendulum.now()
    starting_date = today.start_of('month')
    print(starting_date)
    tomorrows_date = date.today() + timedelta(days = 1)
    print(tomorrows_date)

    #query all users who have completed the word, sorted by number of guesses ascending
    today_word_users = UserWordLink.query.filter(UserWordLink.date >= starting_date, UserWordLink.date < tomorrows_date
    ).join(User).join(Word).order_by(UserWordLink.guesses).all()

    return jsonify({'initials' : [today_word_user.user.initials for today_word_user in today_word_users],
                    'guesses': [today_word_user.guesses for today_word_user in today_word_users]})

@bp.route('/update_database', methods=['POST'])
def update_database():
    
    req = request.get_json()
    word = req['wordle'].lower()
    guesses = req['guesses']
    print(word)
    print(guesses)

    user = User.query.filter_by(id=current_user.id).first()

    word = Word.query.filter_by(name=word).first()
    if word == None:
        word = Word(name=word)
        db.session.add(word)
        db.session.commit()

    user_word = UserWordLink(user_id=user.id, word_id=word.id, guesses=guesses)
    user_words = UserWordLink.query.all()
    
    if user_word not in user_words:
        db.session.add(user_word)
        db.session.commit()

    response_data = {
        "success": True,
        "status_code": 200,             
        }  

    return jsonify(response_data)
