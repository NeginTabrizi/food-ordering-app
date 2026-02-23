import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import Ui_Form
from controller import AppController
from app import FoodApp
from models.restaurant import Restaurant
from models.food import Food

def main():
    logic = FoodApp()

    r1 = Restaurant("کافه رستوران حس نو")
    r1.add_food(Food("پیتزا پپرونی", 880000))
    r1.add_food(Food("پیتزا مارگاریتا", 850000))
    r1.add_food(Food("پیتزا سیر و استیک", 950000))
    r1.add_food(Food("پیتزا گوشت و قارچ", 750000))
    r1.add_food(Food("پیتزا آلفردو", 850000))
    r1.add_food(Food("سالاد سزار", 770000))
    r1.add_food(Food("سیب زمینی", 250000))
    r1.add_food(Food("انواع نوشیدنی", 50000))


    r2 = Restaurant("جیگرکی جیگرگوشه")
    r2.add_food(Food("کوبیده", 220000))
    r2.add_food(Food("جوجه", 240000))
    r2.add_food(Food("جیگر", 140000))
    r2.add_food(Food("دل", 120000))
    r2.add_food(Food("قلوه", 130000))
    r2.add_food(Food("پنیر کبابی", 50000))
    r2.add_food(Food("دوغ یا نوشابه", 40000))

    r3 = Restaurant("کافه دارچین")
    r3.add_food(Food("چایی", 120000))
    r3.add_food(Food("قهوه آمریکانو", 220000))
    r3.add_food(Food("آیس کارامل ماکیاتو", 320000))
    r3.add_food(Food("آیس لاته", 240000))
    r3.add_food(Food("تیرامیسو", 380000))
    r3.add_food(Food("چیزکیک سن سباستین", 360000))
    r3.add_food(Food("چیزکیک نیویورکی", 320000))
    r3.add_food(Food("کیک روز", 250000))

    logic.add_restaurant(r1)
    logic.add_restaurant(r2)
    logic.add_restaurant(r3)

    from PyQt5.QtWidgets import QApplication, QWidget
    from ui.main_window import Ui_Form
    from controller import AppController

    app = QApplication(sys.argv)

    main_window = QWidget()
    ui = Ui_Form()
    ui.setupUi(main_window)

    controller = AppController(logic, ui)

    main_window.show()
    sys.exit(app.exec_())





if __name__ == "__main__":
    main()