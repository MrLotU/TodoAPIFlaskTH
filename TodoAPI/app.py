from flask import Flask, g, jsonify, render_template, request, redirect, session
from TodoAPI.resources import todo_api
from .sql import init_db
from .util.auth import Auth
from .models.user import User, HASHER

app = Flask(__name__)
app.register_blueprint(todo_api, url_prefix='/api/v1')
app.secret_key = 'MuchSecret,wow'

@app.route('/')
@Auth.form_auth
def my_todos():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            user = User.get(User.username**username)
        except User.DoesNotExist:
            return render_template('login.html', message='Unknown username, try signing up instead?')
        else:
            if user.verify_password(password):
                g.user = user
                return redirect('/')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        pass1 = request.form.get('pass1')
        pass2 = request.form.get('pass2')
        if pass1 != pass2:
            return render_template('signup.html', message='Passwords don\'t match')
        try:
            user = User.get(User.username**username)
        except User.DoesNotExist:
            user = User.create_user(username, pass1)
            g.user = user
            return redirect('/')
        else:
            return render_template('signup.html', message='User with that username already exists')
    return render_template('signup.html')

@app.route('/logout')
def logout():
    g.user = None
    return redirect('/login')

@app.route('/api/v1/auth/token')
@Auth.form_auth
def get_token():
    return g.user.auth_token

@app.before_first_request
def setup():
    init_db()

@app.before_request
def check_auth():
    g.user = None
    if 'token' in session:
        g.user = User.verify_auth_token(session.get('token'))

@app.after_request
def save_auth(response):
    if g.user and 'token' not in session:
        session['token'] = g.user.generate_auth_token()
    elif not g.user and 'token' in session:
        del session['token']

    return response

@app.context_processor
def inject_data():
    return dict(
        user=g.user,
    )