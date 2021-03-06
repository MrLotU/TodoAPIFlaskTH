from flask import g, redirect, request
import gevent
import functools
from werkzeug.http import parse_authorization_header

from flask_httpauth import HTTPBasicAuth

from TodoAPI.models.user import User

class Auth:
    """Auth helper class"""
    @staticmethod
    def basic(func):
        """Basic auth provider for Bearer tokens"""
        if callable(func):
            return _check_auth(func)
        else:
            return functools.partial(_check_auth)
    
    @staticmethod
    def form_auth(func):
        """Basic auth provider for Basic auth"""
        if callable(func):
            return _login_req(func)
        else:
            return functools.partial(_login_req)

def _login_req(func):
    """Checks user login through session"""
    @functools.wraps(func)
    def deco(*args, **kwargs):
        if not hasattr(g, 'user') or not g.user:
            return redirect('/login')
        return func(*args, **kwargs)
    return deco

def _check_auth(func):
    """Checks user login through Auth headers"""
    @functools.wraps(func)
    def deco(*args, **kwargs):
        if 'Authorization' in request.headers:
            try:
                scheme, creds = request.headers['Authorization'].split(
                    None, 1
                )
            except ValueError:
                return '', 401
            else:
                if scheme == 'Bearer':
                    user = User.verify_auth_token(creds)
                    if user is not None:
                        g.user = user
                        return func(*args, **kwargs)
        return '', 401
    return deco