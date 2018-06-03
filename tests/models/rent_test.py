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
    bike = Bike("red")
    rent_type = RentPerDay(5.00)

    def test_creation(self):
        rent = self._create_rent()
        self.assertEqual(str(rent.cost()), '120.0')

    def test_raise_invalid_creation_with_message(self):
        msg = 'Subclass must implement abstract method'
        try:
            rent = self._create_rent()
            rent._validates_users(None)
        except NotImplementedError as e:
            self.assertEqual(str(e), msg)

    def _create_rent(self):
        return Rent(self.rent_type, self.user1, self.bike, self.start, self.end)
