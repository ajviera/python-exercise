from src.models.user import *
from src.models.bike import *
from src.models.rent import *
from src.models.rent_per_day import *
from src.models.rent_type import *
import datetime
from datetime import timedelta
import unittest

class RentTest(unittest.TestCase):
    end = datetime.datetime.now()
    start = end - timedelta(1)
    user1 = User("A")
    user2 = User("B")
    user3 = User("C")
    user4 = User("C")
    user5 = User("C")
    user6 = User("C")
    bike = Bike("red")
    rent_type = RentPerDay(5.00)

    def test_creation(self):
        rent = Rent(
            self.rent_type, self.user1, self.bike, self.start, self.end)
        self.assertEqual(str(rent.cost()), '120.0')

    def test_raise_invalid_creation_with_message(self):
        msg = 'Users must be only one'
        try:
            self._create_invalid_rent()
        except ValueError as e:
            self.assertEqual(str(e), msg)

    def _create_invalid_rent(self):
        return Rent(
            self.rent_type,
            [self.user1, self.user2, self.user3],
            self.bike,
            self.start,
            self.end
        )
