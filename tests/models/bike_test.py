from src.models.bike import *
import unittest

class BikeTest(unittest.TestCase):
    def test_creation(self):
        detail = 'red'
        bike = Bike(detail)
        self.assertEqual(bike.detail, detail)
