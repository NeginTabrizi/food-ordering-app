from models.user import User
from models.restaurant import Restaurant
from models.food import Food


class FoodApp:
    def __init__(self):
        self.restaurants = []

    def add_restaurant(self, restaurant):
        self.restaurants.append(restaurant)

    def show_restaurants(self):
        print("\n🍽 لیست رستوران‌ها:")
        for index, restaurant in enumerate(self.restaurants, start=1):
            print(f"{index}. {restaurant.name}")

    def run(self):
        # ساخت کاربر
        name = input("👤 نام خود را وارد کنید: ")
        user = User(name)

        while True:
            self.show_restaurants()
            choice = input("شماره رستوران (0 = پایان سفارش): ")

            if not choice.isdigit():
                print("❌ لطفاً عدد وارد کنید")
                continue

            choice = int(choice)

            if choice == 0:
                break

            if choice > len(self.restaurants):
                print("❌ رستوران نامعتبر")
                continue

            restaurant = self.restaurants[choice - 1]
            restaurant.show_menu()

            food_choice = input("شماره غذا (0 = بازگشت): ")

            if not food_choice.isdigit():
                print("❌ لطفاً عدد وارد کنید")
                continue

            food_choice = int(food_choice)

            if food_choice == 0:
                continue

            if food_choice > len(restaurant.menu):
                print("❌ غذای نامعتبر")
                continue

            selected_food = restaurant.menu[food_choice - 1]
            user.order.add_item(selected_food)

            print(f"✅ {selected_food.name} به سفارش اضافه شد")

        user.order.show_order()
        print("🙏 ممنون از سفارش شما")