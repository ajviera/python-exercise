import datetime

class Rent:
    def __init__(self, rent_type, users, bike, start_time):
        self.rent_type = rent_type
        self.users = users
        self.bike = bike
        self.start_time = start_time
        self.end_time = None

    def close(self):
        self.end_time = datetime.datetime.now()
        return self._cost()

    def partial_cost(self):
        response = self.close()
        self.end_time = None
        return response

    def _cost(self):
        return round((self.rent_type.price * self._total_time()), 2)

    def _total_time(self):
        diff = self.end_time - self.start_time
        return diff.days * 24 + diff.seconds // 3600

    def _validates_users(self, users):
        raise NotImplementedError('Subclass must implement abstract method')
