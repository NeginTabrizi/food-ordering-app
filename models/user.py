from models.order import Order

class User:
    def __init__(self, name):
        self.name = name
        self.order = Order()