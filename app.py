from flask import Flask
from db import db
from routes import register_routes

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
register_routes(app)

with app.app_context():
    db.create_all()
    print(db.metadata.tables.keys())

if __name__ == '__main__':
    app.run(debug=True)