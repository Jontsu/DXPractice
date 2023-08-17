from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def initialise_database():
    from models import Users, Exercises
    # db.drop_all()
    db.create_all()