from TodoAPI.app import app
from TodoAPI.models import Todo

from unittest import TestCase, main as execute_tests

class TestAPI(TestCase):
    def setup(self):
        self.client = app.test_client()

    def test_index(self):
        r = self.client.get('/api/v1/todos')
        print(r.json)

if __name__ == '__main__':
    execute_tests()