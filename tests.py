from TodoAPI.app import app
from TodoAPI.models import Todo
from TodoAPI.sql import init_db
import sys

from unittest import TestCase, main as execute_tests

class TestAPI(TestCase):
    def setUp(self):
        init_db()
        self.client = app.test_client()

    def test_index(self):
        r = self.client.get('/api/v1/todos')
        print(r.status_code)

if __name__ == '__main__':
    execute_tests()