class RentType:
    def __init__(self, price):
        self.price = price

    def __str__(self):
        raise NotImplementedError('Subclass must implement abstract method')
