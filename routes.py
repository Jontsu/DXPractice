from flask import render_template, request, redirect, url_for, session
from components import users, exercises


def register_routes(app):

    @app.route('/')
    def index_route():
        all_exercises = exercises.get_all_exercises()
        return render_template('index.html', exercises=all_exercises)

    @app.route('/register', methods=['GET', 'POST'])
    def register_route():
        error = None
        if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')
            password1 = request.form.get('password1')
            password2 = request.form.get('password2')
            role = request.form.get('role')
            
            if not username or not email or not password1 or not password2 or not role:
                error = "All fields are required"
            elif password1 != password2:
                error = "Passwords do not match"
            elif len(password1) < 4:
                error = "Password should be at least 8 characters long"

            if not error:
                try:
                    users.register_user(username, email, password1, role)
                    session['username'] = username
                    return redirect(url_for('index_route'))
                except Exception as e:
                    error = f"Unexpected error occurred: {str(e)}"

        csrf_token = users.get_or_create_csrf_token()
        return render_template('register.html', error=error, csrf_token=csrf_token)

    @app.route('/login', methods=['GET', 'POST'])
    def login_route():
        error = None
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            if not username or not password:
                error = "Both username and password are required"
            else:
                try:
                    if users.login_user(username, password):
                        session['username'] = username
                        return redirect(url_for('index_route'))
                    else:
                        error = "Invalid credentials"
                except Exception as e:
                    error = f"Unexpected error occurred: {str(e)}"

        csrf_token = users.get_or_create_csrf_token()
        return render_template('login.html', error=error, csrf_token=csrf_token)

    @app.route('/logout')
    def logout_route():
        users.logout_user()
        return redirect(url_for('index_route'))

    @app.route('/exercise/<int:exercise_id>', methods=['GET'])
    def display_exercise_route(exercise_id):
        exercise = exercises.get_exercise_by_id(exercise_id)
        creator = exercises.get_creator_of_exercise(exercise_id)
        return render_template('exercise_display.html', exercise=exercise, creator=creator)

    @app.route('/create_exercise', methods=['GET', 'POST'])
    def create_exercise_route():
        error = None
        if request.method == 'POST':
            users.check_csrf()
            name = request.form.get('name')
            tasks = request.form.get('tasks')

            if not name or not tasks:
                error = "Both name and tasks are required"
            else:
                user = users.get_user_by_username(session['username'])

                if not user or user[4] != 'teacher':
                    return redirect(url_for('index_route'))

                creator_id = user[0]
                try:
                    exercises.create_exercise(name, tasks, creator_id)
                    return redirect(url_for('index_route'))
                except Exception as e:
                    error = f"Unexpected error occurred: {str(e)}"
                
        return render_template('exercise_create.html', error=error)

    @app.route('/exercise/<int:exercise_id>/edit', methods=['GET', 'POST'])
    def edit_exercise_route(exercise_id):
        error = None
        exercise = exercises.get_exercise_by_id(exercise_id)
        
        if not exercise:
            error = "Exercise not found"
            return render_template('index.html', error=error)
        
        creator = exercises.get_creator_of_exercise(exercise_id)
        if session.get('user_id') != creator.id:
            error = "Unauthorised access"
            return render_template('index.html', error=error)

        if request.method == 'POST':
            users.check_csrf()
            name = request.form.get('name')
            tasks = request.form.get('tasks')
            
            if not name or not tasks:
                error = "Both name and tasks are required"
            else:
                try:
                    exercises.update_exercise(exercise_id, name, tasks)
                    return redirect(url_for('display_exercise_route', exercise_id=exercise_id))
                except Exception as e:
                    error = f"Unexpected error occurred: {str(e)}"
        
        return render_template('exercise_edit.html', exercise=exercise, error=error)

    @app.route('/exercise/<int:exercise_id>/delete', methods=['POST'])
    def delete_exercise_route(exercise_id):
        error = None
        if request.method == 'POST':
            users.check_csrf()
            user = users.get_user_by_username(session['username'])

            if not user or user[4] != 'teacher':
                error = "Unauthorised access"

            try:
                exercises.delete_exercise(exercise_id, user[0])
                return redirect(url_for('index_route'))
            except Exception as e:
                error = f"Unexpected error occurred: {str(e)}"
            
        return render_template('index.html', error=error)
