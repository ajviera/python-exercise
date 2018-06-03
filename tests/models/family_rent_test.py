from src.models.user import *
from src.models.bike import *
from src.models.family_rent import *
from src.models.rent_per_day import *
from src.models.rent_type import *
import datetime
from datetime import timedelta
import unittest


class FamilyRentTest(unittest.TestCase):
    end = datetime.datetime.now()
    start = end - timedelta(1)
    user1 = User("A")
    user2 = User("B")
    user3 = User("C")
    user4 = User("D")
    user5 = User("E")
    user6 = User("F")
    bike = Bike("red")
    rent_type = RentPerDay(5.00)

    def test_creation(self):
        family_ren = FamilyRent(
            self.rent_type, [self.user1, self.user2, self.user3], self.bike, self.start)
        self.assertEqual(str(family_ren.close()), '252.0')

    def test_raise_invalid_creation_with_message(self):
        msg = 'Users must be between 3 and 5 members'
        try:
            self._create_invalid_family_rent()
        except ValueError as e:
            self.assertEqual(str(e), msg)

    def _create_invalid_family_rent(self):
        return FamilyRent(
            self.rent_type,
            [self.user1, self.user2, self.user3,
             self.user4, self.user5, self.user6],
            self.bike,
            self.start
        )

