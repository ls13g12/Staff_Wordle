from re import I
from urllib import response
from app.models import User, Word, UserWordLink
from app.main import bp
from app import db
from flask import Flask, render_template, jsonify, request, json
from flask_login import login_required, current_user
from datetime import date, timedelta
from app.main.words import get_new_word
import pendulum
import numpy as np

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    return render_template('index.html')


def check_word_completed_today(word):
    today = date.today()
    user = User.query.filter_by(id=current_user.id).first()
    word = Word.query.filter_by(name=word).first()
    user_word = UserWordLink.query.filter(UserWordLink.user_id == user.id, UserWordLink.word_id == word.id, UserWordLink.date >= today).first()
    if user_word: 

        return True
    return False


@bp.route('/get_word', methods = ["GET","POST"])
@login_required
def get_word():

    today = date.today()
    todays_user_word = UserWordLink.query.join(Word).filter(UserWordLink.date >= today).first()

    if todays_user_word:
        word = todays_user_word.word.name
        is_word_completed_today = check_word_completed_today(word)
        if is_word_completed_today:
            word = None

    else:
        is_new_word = False

        while not is_new_word:
            word = get_new_word()
            word = Word(name=word)
            word_query = Word.query.filter_by(name=word).first()
            
            if not word_query:
                is_new_word = True
                db.session.add(word)
                db.session.commit()
        
        word = word.name

    return jsonify({'data': word})


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
    week_word_users = UserWordLink.query.filter(UserWordLink.date >= starting_date, UserWordLink.date < tomorrows_date
    ).join(User).join(Word).order_by(UserWordLink.guesses).all()

    initials_arr, average_guesses_arr = get_user_and_average(week_word_users)

    return jsonify({'initials' : initials_arr, 'guesses': average_guesses_arr})


#find average of score for each user
def get_user_and_average(user_word_link_query):
    word_users = user_word_link_query
    user_guesses = {}
    for word_user in word_users:
        if word_user.user.initials not in user_guesses:
            user_guesses.update({word_user.user.initials: [word_user.guesses]})
        else:
            user_guesses[word_user.user.initials].append(word_user.guesses)

    average_guesses_arr = []
    for initials in user_guesses:
        average_guesses_arr.append([initials, round(np.average(user_guesses[initials]), 2)])
    
    average_guesses_arr.sort(key=lambda x:x[1])

    #returns 1D array of initials and 1D array of average guess attempts
    return [array[0] for array in average_guesses_arr], [array[1] for array in average_guesses_arr]


@bp.route('/month_leaderboard_data')
@login_required
def month_leaderboard_data():
    today = pendulum.now()
    starting_date = today.start_of('month')
    tomorrows_date = date.today() + timedelta(days = 1)

    #query all users who have completed the word, sorted by number of guesses ascending
    month_word_users = UserWordLink.query.filter(UserWordLink.date >= starting_date, UserWordLink.date < tomorrows_date
    ).join(User).join(Word).order_by(UserWordLink.guesses).all()

    initials_arr, average_guesses_arr = get_user_and_average(month_word_users)

    return jsonify({'initials' : initials_arr, 'guesses': average_guesses_arr})

@bp.route('/all_leaderboard_data')
@login_required
def all_leaderboard_data():
    #query all users
    all_word_users = UserWordLink.query.all()

    initials_arr, average_guesses_arr = get_user_and_average(all_word_users)

    return jsonify({'initials' : initials_arr, 'guesses': average_guesses_arr})

@bp.route('/update_database', methods=['POST'])
def update_database():
    
    req = request.get_json()
    word = req['wordle'].lower()
    guesses = req['guesses']

    user = User.query.filter_by(id=current_user.id).first()

    word = Word.query.filter_by(name=word).first()
    if not word:
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
