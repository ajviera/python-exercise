class UsersController(object):
    def __init__(self, db):
        self.db = db

    def index(self):
        return self._serialize_users(self.db.get_users())

    def show(self, id):
        return self._serialize_user(self.db.get_user(id))

    def _serialize_user(self, user):
        return user.to_json()

    def _serialize_users(self, users):
        serialize = []
        for user in users:
            serialize.append(user.to_json())
        return serialize
