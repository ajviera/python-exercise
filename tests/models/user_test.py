from src.models.user import *
import unittest

class UserTest(unittest.TestCase):
    def test_creation(self):
        name = 'Ariel'
        user = User(name)
        self.assertEqual(user.name, name)

