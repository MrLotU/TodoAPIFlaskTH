from flask import Flask, g, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def my_todos():
    return render_template('index.html')