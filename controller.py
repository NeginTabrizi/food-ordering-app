from models.user import User

class AppController:
    def __init__(self, logic, ui):
        self.logic = logic
        self.ui = ui
        self.user = User("User")

        self.load_restaurants()

        self.ui.restaurantBox.currentIndexChanged.connect(self.load_menu)
        self.ui.addButton.clicked.connect(self.add_food)
        self.ui.removeButton.clicked.connect(self.remove_food)

    def load_restaurants(self):
        for r in self.logic.restaurants:
            self.ui.restaurantBox.addItem(r.name)
        self.load_menu()

    def load_menu(self):
        self.ui.menuList.clear()
        restaurant = self.logic.restaurants[self.ui.restaurantBox.currentIndex()]
        for food in restaurant.menu:
            self.ui.menuList.addItem(f"{food.name} - {food.price} تومان")

    def add_food(self):
        f_index = self.ui.menuList.currentRow()
        if f_index == -1:
            return

        qty = self.ui.quantitySpin.value()
        r_index = self.ui.restaurantBox.currentIndex()
        food = self.logic.restaurants[r_index].menu[f_index]

        self.user.order.add_item(food, qty)
        self.refresh_order()

    def remove_food(self):
        row = self.ui.orderList.currentRow()
        if row == -1:
            return

        food = list(self.user.order.items.keys())[row]
        self.user.order.remove_item(food)
        self.refresh_order()

    def refresh_order(self):
        self.ui.orderList.clear()
        for food, qty in self.user.order.items.items():
            self.ui.orderList.addItem(f"{food.name} × {qty}")

        self.ui.totalLabel.setText(
            f"مبلغ کل: {self.user.order.total_price()} تومان"
        )