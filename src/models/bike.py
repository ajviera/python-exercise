class Bike(object):
    def __init__(self, id, detail):
        self.id = id
        self.detail = detail

    def __str__(self):
        return self.detail

    def to_json(self):
        return {'id': str(self.id), 'name': str(self.detail)}
