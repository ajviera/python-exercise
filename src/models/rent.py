import datetime


class Rent(object):
    def __init__(self, id, rent_type, users, bike, start_time):
        self.id = id
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

    def __str__(self):
        return str(self.id)

    def _validates_users(self, users):
        raise NotImplementedError('Subclass must implement abstract method')

    def to_json(self):
        return {
            'id': self.id,
            'rent_type': self.rent_type.to_json(),
            'users': self._get_users(),
            'bike': self.bike.to_json(),
            'start_time': self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            'end_time': self._end_time(),
            'class': self.__class__.__name__
        }

    def _end_time(self):
        if self.end_time != None:
            return self.end_time.strftime("%Y-%m-%d %H:%M:%S")
