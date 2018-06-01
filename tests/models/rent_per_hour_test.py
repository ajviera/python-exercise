from src.models.rent_per_hour import *
import unittest

class RentPerHourTest(unittest.TestCase):
    price = 5

    def test_creation(self):
        rent_per_hour = self._create_rent_per_hour()
        self.assertEqual(rent_per_hour.price, self.price)

    def test_to_string(self):
        msg1 = '$' + str(self.price) + ' per day'
        msg2 = '$' + str(self.price) + ' per hour'
        msg3 = '$' + str(self.price) + ' per week'
        rent_per_hour = self._create_rent_per_hour()

        self.assertNotEqual(str(rent_per_hour), msg1)
        self.assertEqual(str(rent_per_hour), msg2)
        self.assertNotEqual(str(rent_per_hour), msg3)

    def _create_rent_per_hour(self):
        return RentPerHour(self.price)
