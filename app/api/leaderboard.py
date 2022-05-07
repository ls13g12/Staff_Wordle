from app.models import User, Word, UserWordLink
from app.api import bp
from app import db
from flask import jsonify, make_response, request
from flask_login import login_required, current_user
from datetime import date, timedelta
import pendulum
import numpy as np


@bp.route("/api/leaderboard/", methods=["GET"])
@login_required
def leaderboard_api():
    filter = request.args["filter"]

    if filter == "today":
        starting_date = date.today()
        tomorrows_date = date.today() + timedelta(days=1)

        # query all users who have completed the word, sorted by number of guesses ascending
        word_users = (
            UserWordLink.query.filter(
                UserWordLink.date >= starting_date, UserWordLink.date < tomorrows_date
            )
            .join(User)
            .join(Word)
            .order_by(UserWordLink.guesses)
            .all()
        )

    elif filter == "week":
        today = pendulum.now()
        starting_date = today.start_of("week")
        tomorrows_date = date.today() + timedelta(days=1)

        # query all users who have completed the word, sorted by number of guesses ascending
        word_users = (
            UserWordLink.query.filter(
                UserWordLink.date >= starting_date, UserWordLink.date < tomorrows_date
            )
            .join(User)
            .join(Word)
            .order_by(UserWordLink.guesses)
            .all()
        )

    elif filter == "month":
        today = pendulum.now()
        starting_date = today.start_of("month")
        tomorrows_date = date.today() + timedelta(days=1)

        # query all users who have completed the word, sorted by number of guesses ascending
        word_users = (
            UserWordLink.query.filter(
                UserWordLink.date >= starting_date, UserWordLink.date < tomorrows_date
            )
            .join(User)
            .join(Word)
            .order_by(UserWordLink.guesses)
            .all()
        )

    else:
        # query all users
        word_users = UserWordLink.query.all()

    initials_arr, average_guesses_arr = get_user_and_average(word_users)

    return make_response(
        jsonify({"initials": initials_arr, "guesses": average_guesses_arr}), 200
    )


# find average of score for each user
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
        count = len(user_guesses[initials])
        initials_and_count = initials + " (" + str(count) + ")"
        average_guesses_arr.append(
            [initials_and_count, round(np.average(user_guesses[initials]), 2)]
        )

    average_guesses_arr.sort(key=lambda x: x[1])

    # returns 1D array of initials and 1D array of average guess attempts
    return [array[0] for array in average_guesses_arr], [
        array[1] for array in average_guesses_arr
    ]


@bp.route("/update_database", methods=["POST"])
def update_database():

    req = request.get_json()
    word = req["wordle"].lower()
    guesses = req["guesses"]

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
