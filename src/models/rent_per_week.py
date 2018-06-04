from .rent_type import *

class RentPerWeek(RentType):
    def __str__(self):
        return ('$' + str(self.price) + ' per week')

    def to_json(self):
        return str({'id': str(self.id), 'price': str(self.price), 'type': 'per_week'})
