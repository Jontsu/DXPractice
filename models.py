from sqlalchemy.schema import UniqueConstraint

from db import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    github_handle = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    role = db.Column(db.Text, nullable=False)


class Exercises(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.Text, unique=True, nullable=False)
    tasks = db.Column(db.Text, nullable=False)
    

class Solutions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    submitter_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    solution_link = db.Column(db.Text)
    comment_link_1 = db.Column(db.Text)
    comment_link_2 = db.Column(db.Text)
    comment_link_3 = db.Column(db.Text)

    __table_args__ = (UniqueConstraint('submitter_id', 'exercise_id', name='unique_submitter_exercise'),)
