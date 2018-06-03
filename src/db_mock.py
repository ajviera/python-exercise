from models.user import *
from models.bike import *
from models.rent_per_day import *
from models.rent_per_hour import *
from models.rent_per_week import *
from models.family_rent import *
from models.normal_rent import *
from datetime import datetime

class DbMock():
    def __init__(self):
        self._set_models()

    def get_users(self):
        users = [
            self.user1,
            self.user2,
            self.user3,
            self.user4,
            self.user5,
            self.user6
        ]
        return users

    def get_user(self, id):
        return self._find_user(id)

    def close_user_rent(self, user_id, rent_id):
        rent = self._find_rent(rent_id)
        self._validate_user_has_rent(user_id, rent)
        rent.close()
        return rent

    def create_rent(self, id, time, extra_users, bike_id, rent_class):
        user = self._find_user(id)
        rent_type = self._find_rent_type(time)
        bike = self._find_bike(bike_id)
        if rent_class == 'normal':
            rent = NormalRent(
                (self.rents[-1].id + 1), rent_type, user, bike, datetime.now())
        elif rent_class == 'family':
            users = [user]
            for extra_user in extra_users:
                users.append(self._find_user((extra_user['id'])))
            rent = FamilyRent(
                (self.rents[-1].id + 1), rent_type, users, bike, datetime.now())

        self.rents.append(rent)

    def get_user_rent(self, user_id, rent_id):
        rent = self._find_rent(rent_id)
        self._validate_user_has_rent(user_id, rent)
        return rent

    def get_user_rents(self, id):
        user = self._find_user(id)
        if user != None:
            return self._find_user_rents(user)

    def _find_user_rents(self, user):
        rents = []
        for rent in self.rents:
            if type(rent) == FamilyRent:
                if user in rent.users:
                    rents.append(rent)

            if type(rent) == NormalRent:
                if user == rent.users:
                    rents.append(rent)
        return rents

    def _find_rent_type(self, time):
        if 'per_hour' == time:
            return self.rent_types[0]
        elif 'per_day' == time:
            return self.rent_types[1]
        else:
            return self.rent_types[2]
        raise NameError('The rent_type does not exist')

    def _find_user(self, id):
        for user in self.users:
            if int(user.id) == id:
                return user
        raise NameError('The user does not exist')

    def _find_bike(self, id):
        for bike in self.bikes:
            if int(bike.id) == id:
                return bike
        raise NameError('The bike does not exist')

    def _find_rent(self, id):
        for rent in self.rents:
            if int(rent.id) == id:
                return rent
        raise NameError('The rent does not exist')

    def _validate_user_has_rent(self, user_id, rent):
        rents = self.get_user_rents(user_id)
        return rent in rents

    def _set_models(self):
        self.start = datetime.now()
        self.user1 = User(1, 'A')
        self.user2 = User(2, 'B')
        self.user3 = User(3, 'C')
        self.user4 = User(4, 'D')
        self.user5 = User(5, 'E')
        self.user6 = User(6, 'F')

        self.bike1 = Bike(1, 'red')
        self.bike2 = Bike(2, 'red')
        self.bikes = [self.bike1, self.bike2]
        self.rent_type1 = RentPerHour(1, 5.00)
        self.rent_type2 = RentPerDay(2, 20.00)
        self.rent_type3 = RentPerWeek(3, 60.00)
        self.rent_types = [self.rent_type1, self.rent_type2, self.rent_type3]

        self.rent1 = FamilyRent(
            1, self.rent_type1, [self.user1, self.user2, self.user3], self.bike1, self.start)
        self.rent2 = NormalRent(
            2, self.rent_type2, self.user1, self.bike1, self.start)
        self.rent3 = FamilyRent(
            3, self.rent_type3, [self.user1, self.user2, self.user3], self.bike2, self.start)
        self.rents = [self.rent1, self.rent2, self.rent3]

        self.users = [
            self.user1,
            self.user2,
            self.user3,
            self.user4,
            self.user5,
            self.user6
        ]
