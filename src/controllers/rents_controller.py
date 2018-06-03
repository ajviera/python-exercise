class RentsController(object):
    def __init__(self, db):
        self.db = db

    def get_user_rents(self, user_id):
        return self._serialize_rents(self.db.get_user_rents(user_id))

    def get_user_rent(self, user_id, rent_id):
        return self._serialize_rent(self.db.get_user_rent(user_id, rent_id))

    def close_user_rent(self, user_id, rent_id):
        self.db.close_user_rent(user_id, rent_id)

    def user_rent_a_bike(self, rent_id, params):
        self._validate_rent_params(params)
        self.db.create_rent(rent_id, params["time"],
                            params["extra_users"], params["bike_id"], params["type"])

    def _validate_rent_params(self, params):
        if params["time"] != 'per_day' and params["time"] != 'per_hour' and params["time"] != 'per_week':
            raise ValueError('Time must be per_hour, per_day or per_week')
        if len(params["extra_users"]) != 0 and params["type"] == 'normal':
            raise ValueError('Normal rents only have one user')

    def _serialize_rent(self, rent):
        return rent.to_json()

    def _serialize_rents(self, rents):
        serialize = []
        for rent in rents:
            serialize.append(rent.to_json())
        return serialize
