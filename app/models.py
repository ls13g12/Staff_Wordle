from app import db
from datetime import datetime

class UserWordLink(db.Model):
    __tablename__ = 'user_word_link'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    word_id = db.Column(db.Integer, db.ForeignKey('word.id'), primary_key=True)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)
    guesses = db.Column(db.Integer)

    user = db.relationship("User", back_populates="words")
    word = db.relationship("Word", back_populates="users")


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    words = db.relationship("UserWordLink", back_populates="user")

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Word(db.Model):
    __tablename__ = 'word'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    users = db.relationship("UserWordLink", back_populates="word")
    
    def __repr__(self):
        return '<Word {}>'.format(self.name)



