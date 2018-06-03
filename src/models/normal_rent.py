from .rent import *

class NormalRent(Rent):
    def __init__(self, id,  rent_type, users, bike, start_time):
        self._validates_users(users)
        super().__init__(id, rent_type, users, bike, start_time)

    def _validates_users(self, users):
        if not(type(users) != list):
            raise ValueError('Users must be only one')

    def _get_users(self):
        return self.users.to_json()
