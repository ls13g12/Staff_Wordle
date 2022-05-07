from app import db, login
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class UserWordLink(db.Model):
    __tablename__ = "user_word_link"
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    word_id = db.Column(db.Integer, db.ForeignKey("word.id"), primary_key=True)
    date = db.Column(db.DateTime, default=date.today())
    guesses = db.Column(db.Integer)

    user = db.relationship("User", back_populates="words")
    word = db.relationship("Word", back_populates="users")


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    initials = db.Column(db.String(3), index=True, unique=True)
    nickname = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))
    words = db.relationship("UserWordLink", back_populates="user")

    def __repr__(self):
        return "<User {}>".format(self.nickname)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Word(db.Model):
    __tablename__ = "word"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    users = db.relationship("UserWordLink", back_populates="word")
    word_log = db.relationship("WordLog", backref="word", lazy="dynamic")

    def __repr__(self):
        return "<Word {}>".format(self.name)


class WordLog(db.Model):
    __tablename__ = "word_log"
    id = db.Column(db.Integer, primary_key=True)
    word_id = db.Column(db.Integer, db.ForeignKey("word.id"), nullable=True)
    date = db.Column(db.DateTime, default=date.today())

    def __repr__(self):
        return "<Word {} on date {}>".format(self.word, self.date)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
