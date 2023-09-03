import os
from flask import abort, request, session
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash

from db import db


def get_all_users():
    sql = text("""
        SELECT * 
        FROM users
    """)
    result = db.session.execute(sql)
    return result.fetchall()


def get_user_by_github_handle(github_handle):
    try:
        sql = text("""
            SELECT * 
            FROM users 
            WHERE github_handle = :github_handle
        """)
        result = db.session.execute(sql, {"github_handle": github_handle})
        user = result.fetchone()
        return user
    except Exception as e:
        raise Exception(f"Error fetching user details: {str(e)}")


def get_all_permitted_users():
    permitted_teachers_sql = text("SELECT github_handle, 'teacher' as role FROM permitted_teachers")
    permitted_students_sql = text("SELECT github_handle, 'student' as role FROM permitted_students")
    teachers = db.session.execute(permitted_teachers_sql).fetchall()
    students = db.session.execute(permitted_students_sql).fetchall()
    return teachers + students


def is_permitted(github_handle, role):
    table_name = "permitted_teachers" if role == "teacher" else "permitted_students"
    sql = text(f"SELECT * FROM {table_name} WHERE github_handle = :github_handle")
    result = db.session.execute(sql, {"github_handle": github_handle})
    return result.fetchone() is not None


def add_permitted_user(github_handle, role):
    table_name = "permitted_teachers" if role == "teacher" else "permitted_students"
    sql = text(f"INSERT INTO {table_name} (github_handle) VALUES (:github_handle)")
    db.session.execute(sql, {"github_handle": github_handle})
    db.session.commit()


def delete_permitted_user(github_handle):
    for table_name in ["permitted_teachers", "permitted_students"]:
        sql = text(f"DELETE FROM {table_name} WHERE github_handle = :github_handle")
        db.session.execute(sql, {"github_handle": github_handle})
    db.session.commit()


def add_permission_request(github_handle, requested_role):
    try:
        sql = text("""
            INSERT INTO permission_requests (github_handle, requested_role, status) 
            VALUES (:github_handle, :requested_role, 'pending')
        """)
        db.session.execute(sql, {"github_handle": github_handle, "requested_role": requested_role})
        db.session.commit()
    except Exception as e:
        raise Exception(f"Error adding permission request: {str(e)}")


def get_pending_permission_requests():
    sql = text("SELECT * FROM permission_requests WHERE status = 'pending'")
    result = db.session.execute(sql)
    return result.fetchall()


def get_permission_request_status(github_handle):
    sql = text("""
        SELECT status 
        FROM permission_requests 
        WHERE github_handle = :github_handle
    """)
    result = db.session.execute(sql, {"github_handle": github_handle})
    request_status = result.fetchone()
    return request_status[0] if request_status else None


def update_request_status(request_id, status):
    sql = text("UPDATE permission_requests SET status = :status WHERE id = :id")
    db.session.execute(sql, {"status": status, "id": request_id})
    db.session.commit()


def register_user(github_handle, password):

    if not get_all_users():
        role = "teacher"
        add_permitted_user(github_handle, role)
    else:
        if is_permitted(github_handle, "teacher"):
            role = "teacher"
        elif is_permitted(github_handle, "student"):
            role = "student"
        else:
            permission_status = get_permission_request_status(github_handle)
            if permission_status == "pending":
                raise Exception("Your permission request is pending. Please try again tomorrow or contact your teacher.")
            elif permission_status == "rejected":
                raise Exception("Your permission request has been rejected. Please contact your teacher.")
            else:
                raise Exception("GitHub handle not permitted. Please request permission.")
    
    hashed_password = generate_password_hash(password)
    try:
        sql = text("""
            INSERT INTO users (github_handle, password, role) 
            VALUES (:github_handle, :password, :role)
        """)
        db.session.execute(sql, {"github_handle": github_handle, "password": hashed_password, "role": role})
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise Exception("Github handle already exists.")
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Error registering user: {str(e)}")
    

def login_user(github_handle, password):

    user_data = get_user_by_github_handle(github_handle)

    if not user_data or not is_permitted(user_data[1], user_data[3]):
        raise Exception("GitHub handle not permitted. Please request permission.")

    try:
        sql = text("""
            SELECT password 
            FROM users 
            WHERE github_handle = :github_handle
        """)
        result = db.session.execute(sql, {"github_handle": github_handle})
        user = result.fetchone()

        if user and check_password_hash(user[0], password):
            session["user_id"] = user_data[0]
            session["github_handle"] = github_handle
            session["role"] = user_data[3]
            session["csrf_token"] = get_or_create_csrf_token()
            return True
        
        return False
    except Exception as e:
        raise Exception(f"Error logging in: {str(e)}")


def logout_user():
    keys_to_delete = ['user_id', 'github_handle', 'role', 'csrf_token']
    for key in keys_to_delete:
        try:
            del session[key]
        except KeyError:
            pass


def get_or_create_csrf_token():
    if "csrf_token" not in session:
        session["csrf_token"] = os.urandom(16).hex()
    return session["csrf_token"]


def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
