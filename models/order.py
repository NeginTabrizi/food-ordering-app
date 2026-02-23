class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, food, quantity):
        if food in self.items:
            self.items[food] += quantity
        else:
            self.items[food] = quantity

    def remove_item(self, food):
        if food in self.items:
            del self.items[food]

    def total_price(self):
        return sum(food.price * qty for food, qty in self.items.items())