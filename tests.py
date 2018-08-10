from TodoAPI.app import app
from TodoAPI.models import Todo
from TodoAPI.sql import init_db
import sys

from unittest import TestCase, main as execute_tests

class TestAPI(TestCase):
    def setUp(self):
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
    
    def test_api(self):
        r = self.client.post('/login', data=dict(
            username='temp',
            password='pass'
        ))
        self.assertEqual(r.status_code, 302)
        tr = self.client.get('/api/v1/auth/token')
        self.assertEqual(tr.status_code, 200)
        token = tr.data
        r = self.client.get('/api/v1/todos', headers=dict(
            Authorization='Bearer {}'.format(token)
        ))


if __name__ == '__main__':
    execute_tests()