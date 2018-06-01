from models.user import *
import unittest

class UserTest(unittest.TestCase):
    def test_creation(self):
        user = User('ariel')
        self.assertEqual(user.name, 'ariel')

