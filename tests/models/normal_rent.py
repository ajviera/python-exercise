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
    user1 = User("A")
    user2 = User("B")
    bike = Bike("red")
    rent_type = RentPerDay(5.00)

    def test_creation(self):
        normal_rent = NormalRent(
            self.rent_type, self.user1, self.bike, self.start, self.end)
        self.assertEqual(str(normal_rent.cost()), '120.0')

    def test_raise_invalid_creation_with_message(self):
        msg = 'Users must be only one'
        try:
            self._create_invalid_normal_rent()
        except ValueError as e:
            self.assertEqual(str(e), msg)

    def _create_invalid_normal_rent(self):
        return NormalRent(
            self.rent_type,
            [self.user1, self.user2],
            self.bike,
            self.start,
            self.end
        )
