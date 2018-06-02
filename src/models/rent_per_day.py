from .rent_type import *
class RentPerDay(RentType):
    def __str__(self):
        return ( '$' + str(self.price) + ' per day' )
