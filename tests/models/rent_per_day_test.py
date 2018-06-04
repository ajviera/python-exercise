from src.models.rent_per_day import *
import unittest


class RentPerDayTest(unittest.TestCase):
    price = 20

    def test_creation(self):
        rent_per_day = self._create_rent_per_day()
        self.assertEqual(rent_per_day.price, self.price)

    def test_to_json(self):
        rent_per_day = self._create_rent_per_day()
        self.assertIsNotNone(str(rent_per_day.to_json()))

    def test_to_string(self):
        msg1 = '$' + str(self.price) + ' per day'
        msg2 = '$' + str(self.price) + ' per hour'
        msg3 = '$' + str(self.price) + ' per week'
        rent_per_day = self._create_rent_per_day()

        self.assertEqual(str(rent_per_day), msg1)
        self.assertNotEqual(str(rent_per_day), msg2)
        self.assertNotEqual(str(rent_per_day), msg3)

    def _create_rent_per_day(self):
        return RentPerDay(1, self.price)
