from .rent_type import *
class RentPerHour(RentType):
    def __str__(self):
        return ('$' + str(self.price) + ' per hour')
