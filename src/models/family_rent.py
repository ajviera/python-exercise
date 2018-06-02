from .rent import *
class FamilyRent(Rent):
    def __init__(self, rent_type, users, bike, start_time, end_time):
        print( str(self._validates_users(users)))
        super().__init__(rent_type, users, bike, start_time, end_time)

    def cost(self):
        return round((super().cost() * len(self.users) * 0.70), 2)

    def _validates_users(self, users):
        if not(len(users) >= 3 and len(users) <= 5):
            raise ValueError('Users must be between 3 and 5 members')
