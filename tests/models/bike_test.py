from src.models.bike import *
import unittest

class BikeTest(unittest.TestCase):
    detail = 'red'

    def test_creation(self):
        self.assertEqual(str(self._create_bike()), self.detail)

    def test_to_json(self):
        bike = self._create_bike()
        self.assertEqual(str(bike.to_json()), "{'id': '1', 'name': 'red'}")

    def _create_bike(self):
        return Bike(1, self.detail)
