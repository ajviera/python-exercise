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
    user1 = User(1, 'A')
    user2 = User(2, 'B')
    user3 = User(3, 'C')
    user4 = User(4, 'D')
    user5 = User(5, 'E')
    user6 = User(6, 'F')
    bike = Bike(1, 'red')
    rent_type = RentPerDay(1, 5.00)

    def test_creation(self):
        family_ren = FamilyRent(
            1, self.rent_type, [self.user1, self.user2, self.user3], self.bike, self.start)
        self.assertEqual(str(family_ren.close()), '252.0')

    def test_to_json(self):
        family_rent = self._create_valid_family_rent()
        self.assertIsNotNone(str(family_rent.to_json()))

    def test_to_json_with_closed_rent(self):
        family_rent = self._create_valid_family_rent()
        family_rent.close()
        self.assertIsNotNone(str(family_rent.to_json()))

    def test_raise_invalid_creation_with_message(self):
        msg = 'Users must be between 3 and 5 members'
        try:
            self._create_invalid_family_rent()
        except ValueError as e:
            self.assertEqual(str(e), msg)

    def _create_valid_family_rent(self):
        return FamilyRent(
            1, self.rent_type, [self.user1, self.user2, self.user3], self.bike, self.start)

    def _create_invalid_family_rent(self):
        return FamilyRent(
            1,
            self.rent_type,
            [self.user1, self.user2, self.user3,
             self.user4, self.user5, self.user6],
            self.bike,
            self.start
        )
