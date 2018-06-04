from src.models.user import *
import unittest

class UserTest(unittest.TestCase):
    name = 'Ariel'

    def test_creation(self):
        self.assertEqual(str(self._create_user()), self.name)

    def test_to_json(self):
        user = self._create_user()
        self.assertEqual(str(user.to_json()), "{'id': '1', 'name': 'Ariel'}")

    def _create_user(self):
        return User(1, self.name)
