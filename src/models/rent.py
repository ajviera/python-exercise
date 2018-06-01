from datetime import date
class Rent:
    def __init__(self, rent_type, users, bike, start_time, end_time):
        print(str(self._validates_users(users)))
        self.rent_type = rent_type
        self.users = users
        self.bike = bike
        self.start_time = start_time
        self.end_time = end_time

    def cost(self):
        return round((self.rent_type.price * self._total_time()), 2)

    def _total_time(self):
        diff = self.end_time - self.start_time
        return diff.days * 24 + diff.seconds // 3600

    def _validates_users(self, users):
        if not(type(users) != list):
            raise ValueError('Users must be only one')
