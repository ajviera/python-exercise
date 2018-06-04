from .rent import *
class FamilyRent(Rent):
    def __init__(self, id, rent_type, users, bike, start_time):
        self._validates_users(users)
        super().__init__(id, rent_type, users, bike, start_time)

    def _cost(self):
        return round((super()._cost() * len(self.users) * 0.70), 2)

    def _validates_users(self, users):
        if not(len(users) >= 3 and len(users) <= 5):
            raise ValueError('Users must be between 3 and 5 members')

    def _get_users(self):
        users = []

        for user in self.users:
            users.append(user.to_json())
        return users
