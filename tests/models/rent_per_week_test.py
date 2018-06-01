from src.models.rent_per_week import *
import unittest

class RentPerWeekTest(unittest.TestCase):
    price = 60

    def test_creation(self):
        rent_per_week = self._create_rent_per_week()
        self.assertEqual(rent_per_week.price, self.price)

    def test_to_string(self):
        msg1 = '$' + str(self.price) + ' per day'
        msg2 = '$' + str(self.price) + ' per hour'
        msg3 = '$' + str(self.price) + ' per week'
        rent_per_week = self._create_rent_per_week()

        self.assertNotEqual(str(rent_per_week), msg1)
        self.assertNotEqual(str(rent_per_week), msg2)
        self.assertEqual(str(rent_per_week), msg3)

    def _create_rent_per_week(self):
        return RentPerWeek(self.price)
