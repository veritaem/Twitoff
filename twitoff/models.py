"""SQLalchemy models for Twitoff"""
"""SQLAlchemy models for TwitOff."""

from flask_sqlalchemy import SQLAlchemy 

DB = SQLAlchemy()


class User(DB.Model):
    """Twitter users that we pull and alayze Tweets for."""
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)  # Username of a Twitter User; nullable=False means may not be empty

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Tweet(DB.Model):
    """Tweets."""
    id = DB.Column(DB.Integer, primary_key=True)
    text = DB.Column(DB.Unicode(280))
    user_id = DB.Column(DB.Integer, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return '<Tweet {}>'.format(self.text)