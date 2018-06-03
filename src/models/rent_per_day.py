from .rent_type import *

class RentPerDay(RentType):
    def __str__(self):
        return ('$' + str(self.price) + ' per day')

    def to_json(self):
        return {'id': str(self.id), 'price': str(self.price), 'type': 'per_day'}
