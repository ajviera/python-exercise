import sys
from models.user import *
from models.bike import *
from models.rent import *
from models.family_rent import *
from models.rent_per_hour import *
from models.rent_per_day import *
from models.rent_per_week import *
from models.rent_type import *
import datetime
from datetime import timedelta
end = datetime.datetime.now()
start = end - timedelta(1)

user1 = User("A")
user2 = User("B")
user3 = User("C")
user4 = User("C")
user5 = User("C")
user6 = User("C")
bike = Bike("red")
rent_type = RentPerDay(5.00)

try:
    rent = FamilyRent(
        rent_type, [user1, user2, user3, user4, user5, user6], bike, start, end)
    print(str(rent.cost()))
except ValueError as e:
    print(e)

