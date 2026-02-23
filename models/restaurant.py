from models.food import Food

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_food(self, food):
        self.menu.append(food)

    def show_menu(self):
        print(f"\n📋 منوی {self.name}:")
        for index, food in enumerate(self.menu, start=1):
            print(f"{index}. {food}")