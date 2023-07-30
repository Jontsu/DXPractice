from flask import Flask, render_template
from db import db

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # TODO: Add login logic
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # TODO: Add registration logic
    return render_template('register.html')

@app.route('/exercises')
def exercises():
    # TODO: Fetch and display exercises
    return render_template('exercises.html')

if __name__ == '__main__':
    app.run(debug=True)