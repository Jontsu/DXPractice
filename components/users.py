from db import db
from models import User
from werkzeug.security import check_password_hash, generate_password_hash

def login_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return True
    return False

def register_user(username, email, password, role):
    new_user = User(username=username, email=email, password=password, role=role)
    db.session.add(new_user)
    db.session.commit()
    return True
