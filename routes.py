from flask import render_template, request, redirect, url_for, session
from models import User, Exercise
from components.users import login_user, register_user
from components.exercise import create_exercise, delete_exercise

def register_routes(app):
    @app.route('/')
    def index_route():
        exercises = Exercise.query.all()
        return render_template('index.html', exercises=exercises)

    @app.route('/login', methods=['GET', 'POST'])
    def login_route():
        error=None
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            if login_user(username, password):
                session['username'] = username
                return redirect(url_for('index_route'))
            else:
                error = "Invalid credentials"
        return render_template('login.html', error=error)

    @app.route('/logout')
    def logout_route():
        session.pop('username', None)
        return redirect(url_for('index_route'))

    @app.route('/register', methods=['GET', 'POST'])
    def register_route():
        if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')
            role = request.form.get('role')
            if register_user(username, email, password, role):
                session['username'] = username
                return redirect(url_for('index_route'))
            else:
                raise Exception("Registration failed")
        return render_template('register.html')

    @app.route('/exercise/<int:exercise_id>', methods=['GET'])
    def display_exercise_route(exercise_id):
        exercise = Exercise.query.get(exercise_id)
        creator = User.query.get(exercise.creator_id)
        return render_template('exercise.html', exercise=exercise, creator=creator)

    @app.route('/create_exercise', methods=['GET', 'POST'])
    def create_exercise_route():
        if request.method == 'POST':
            name = request.form.get('name')
            tasks = request.form.get('tasks')
            creator = User.query.filter_by(username=session['username']).first()
            creator_id = creator.id

            if create_exercise(name, tasks, creator_id):
                return redirect(url_for('index_route'))
            else:
                raise Exception("Exercise creation failed")
        return render_template('create_exercise.html')

    @app.route('/exercise/<int:exercise_id>/delete', methods=['POST'])
    def delete_exercise_route(exercise_id):
        creator = User.query.filter_by(username=session['username']).first()

        if delete_exercise(exercise_id, creator.id):
            return redirect(url_for('index_route'))
        else:
            raise Exception("Unauthorized")
