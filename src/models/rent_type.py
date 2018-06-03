class RentType(object):
    def __init__(self, id, price):
        self.id = id
        self.price = price

    def __str__(self):
        raise NotImplementedError('Subclass must implement abstract method')

    def to_json(self):
        raise NotImplementedError('Subclass must implement abstract method')
