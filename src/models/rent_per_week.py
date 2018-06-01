from .rent_type import *
class RentPerWeek(RentType):
    def __str__(self):
        return ('$' + str(self.price) + ' per week')
