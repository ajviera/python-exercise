class User(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.name

    def to_json(self):
        return {'id': str(self.id), 'name': str(self.name)}
