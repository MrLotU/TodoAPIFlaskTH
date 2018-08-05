from flask import Flask, g, jsonify, render_template
from TodoAPI.resources import todo_api
from .sql import init_db

app = Flask(__name__)
app.register_blueprint(todo_api, url_prefix='/api/v1')

@app.route('/')
def my_todos():
    return render_template('index.html')

@app.before_first_request
def setup():
    init_db()