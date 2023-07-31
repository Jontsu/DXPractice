from flask import render_template, request, redirect, url_for
from components.users import login_user, register_user

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            if login_user(username, password):
                return redirect(url_for('index'))
            else:
                return "Invalid credentials", 401
        return render_template('login.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')
            role = request.form.get('role')
            if register_user(username, email, password, role):
                return redirect(url_for('index'))
            else:
                return "Registration failed", 400
        return render_template('register.html')
