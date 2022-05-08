from app.models import User, Word, UserWordLink, WordLog
from app.main import bp
from app import db
from flask import render_template, jsonify, request
from flask_login import login_required, current_user
from datetime import date, timedelta
from app.main.words import get_new_word
import app.main.fullwordlist as fullwordlist
import numpy as np


@bp.route("/")
@bp.route("/index")
@login_required
def index():
    return render_template("index.html")


def check_word_completed_today(word):
    today = date.today()
    user = User.query.filter_by(id=current_user.id).first()
    word = Word.query.filter_by(name=word).first()
    user_word = UserWordLink.query.filter(
        UserWordLink.user_id == user.id,
        UserWordLink.word_id == word.id,
        UserWordLink.date >= today,
    ).first()
    if user_word:
        return True

    return False


@bp.route("/get_word", methods=["GET", "POST"])
@login_required
def get_word():

    # check if there is a stored word in the word log today
    today = date.today()
    todays_word_log = WordLog.query.join(Word).filter(WordLog.date >= today).first()

    if todays_word_log:
        word = todays_word_log.word.name
        is_word_completed_today = check_word_completed_today(word)
        if is_word_completed_today:
            word = None

    # else get new word
    else:
        is_new_word = False

        # while loop to avoid duplicates
        while not is_new_word:
            word = get_new_word()
            word = Word(name=word)
            word_query = Word.query.filter_by(name=word.name).first()

            # if unique word
            if not word_query:
                is_new_word = True
                word_log = WordLog(word=word)
                db.session.add(word)
                db.session.add(word_log)
                db.session.commit()

        word = word.name

    return jsonify({"data": word})


@bp.route("/is_word", methods=["GET", "POST"])
@login_required
def is_word():
    req = request.get_json()
    word = req["word"].lower()
    is_word_bool = fullwordlist.is_word(word)

    return jsonify({"data": is_word_bool})


@bp.route("/leaderboard")
@login_required
def leaderboard():
    return render_template("leaderboard.html")
