from .rent_type import *

class RentPerHour(RentType):
    def __str__(self):
        return ('$' + str(self.price) + ' per hour')

    def to_json(self):
        return str({'id': str(self.id), 'price': str(self.price), 'type': 'per_hour'})
