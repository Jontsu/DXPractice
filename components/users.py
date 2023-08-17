from sqlalchemy import text
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.exc import IntegrityError

from db import db


def get_user_by_username(username):
    sql = text("SELECT * FROM users WHERE username = :username")
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    return user


def login_user(username, password):
    try:
        sql = text("SELECT password FROM users WHERE username = :username")
        result = db.session.execute(sql, {"username": username})
        user = result.fetchone()

        if user and check_password_hash(user[0], password):
            return True
        
        return False
    except Exception as e:
        raise Exception(f"Error logging in: {str(e)}")


def register_user(username, email, password, role):
    hashed_password = generate_password_hash(password)
    try:
        sql = text("INSERT INTO users (username, email, password, role) VALUES (:username, :email, :password, :role)")
        db.session.execute(sql, {"username": username, "email": email, "password": hashed_password, "role": role})
        db.session.commit()
    except IntegrityError:
        raise Exception("Username or Email already exists.")
    except Exception as e:
        raise Exception(f"Error registering user: {str(e)}")
    