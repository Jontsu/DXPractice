from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def initialise_database():
    from models import Users, Exercises, Solutions

    db.create_all()