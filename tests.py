from TodoAPI.app import app
from TodoAPI.models import Todo
from TodoAPI.sql import init_db
import sys

from unittest import TestCase, main as execute_tests

class TestAPI(TestCase):
    def setUp(self):
        """Setup app for testing"""
        init_db()
        self.client = app.test_client()

    def test_index_no_login(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 302)

    def test_index_login(self):
        r = self.client.post('/login', data=dict(
            username='temp',
            password='pass'
        ))
        self.assertEqual(r.status_code, 302)
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)
    
    def test_logout(self):
        r = self.client.post('/login', data=dict(
            username='temp',
            password='pass'
        ))
        self.assertEqual(r.status_code, 302)
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)
        r = self.client.get('/logout')
        self.assertEqual(r.status_code, 302)
        r = self.client.get('/')
        self.assertEqual(r.status_code, 302)
    
    def test_signup(self):
        r = self.client.post('/signup', data=dict(
            username='temp',
            pass1='password',
            pass2='nonMatching'
        ))
        self.assertEqual(r.status_code, 200)
        self.assertIn('Passwords don&#39;t match', r.data.__str__())
        r = self.client.post('/signup', data=dict(
            username='temp',
            pass1='password',
            pass2='password'
        ))
        self.assertEqual(r.status_code, 200)
        self.assertIn('User with that username already exists', r.data.__str__())
        r = self.client.post('/signup', data=dict(
            username='newUser',
            pass1='password',
            pass2='password'
        ))
        self.assertEqual(r.status_code, 200)
    
    
    def test_api(self):
        r = self.client.post('/login', data=dict(
            username='temp',
            password='pass'
        ))
        self.assertEqual(r.status_code, 302)
        tr = self.client.get('/api/v1/auth/token')
        self.assertEqual(tr.status_code, 200)
        # Really ugly but for some reason this gets returned as bytes instead of a string
        token = tr.data.__str__().replace('b\'', '').replace('\'', '')
        headers = {'Authorization': 'Bearer {}'.format(token)}
        r = self.client.get('/api/v1/todos', headers=headers)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json), len(Todo.select()))

if __name__ == '__main__':
    execute_tests()