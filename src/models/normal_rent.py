from .rent import *

class NormalRent(Rent):
    def __init__(self, rent_type, users, bike, start_time, end_time):
        self._validates_users(users)
        super().__init__(rent_type, users, bike, start_time, end_time)

    def _validates_users(self, users):
        if not(type(users) != list):
            raise ValueError('Users must be only one')
