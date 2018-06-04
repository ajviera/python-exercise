from src.models.user import *
from src.models.bike import *
from src.models.normal_rent import *
from src.models.rent_per_day import *
from src.models.rent_type import *
import datetime
from datetime import timedelta
import unittest


class NormalRentTest(unittest.TestCase):
    end = datetime.datetime.now()
    start = end - timedelta(1)
    user1 = User(1, 'A')
    user2 = User(2, 'B')
    bike = Bike(1, 'red')
    rent_type = RentPerDay(1, 5.00)

    def test_creation(self):
        normal_rent = self._create_valid_normal_rent()
        self.assertEqual(str(normal_rent.close()), '120.0')

    def test_to_json(self):
        normal_rent = self._create_valid_normal_rent()
        self.assertIsNotNone(str(normal_rent.to_json()))

    def test_raise_invalid_creation_with_message(self):
        msg = 'Users must be only one'
        try:
            self._create_invalid_normal_rent()
        except ValueError as e:
            self.assertEqual(str(e), msg)

    def _create_valid_normal_rent(self):
        return NormalRent(1, self.rent_type, self.user1, self.bike, self.start)

    def _create_invalid_normal_rent(self):
        return NormalRent(
            1,
            self.rent_type,
            [self.user1, self.user2],
            self.bike,
            self.start
        )
