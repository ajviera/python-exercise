from src.models.rent_type import *
import unittest

class RentTypeTest(unittest.TestCase):
    price = 2

    def test_creation(self):
        rent_type = self._create_rent_type()
        self.assertEqual(rent_type.price, self.price)

    def test_raise_invalid_to_string_with_message(self):
        msg = 'Subclass must implement abstract method'
        try:
            print(str(self._create_rent_type()))
            
        except NotImplementedError as e:
            self.assertEqual(str(e), msg)

    def _create_rent_type(self):
        return RentType(self.price)
