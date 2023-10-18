from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

items = Menu()
coffeemachine = CoffeeMaker()
money = MoneyMachine()

machine_working = True
while machine_working:
    option = input(f"what would you like? ({items.get_items()}): ").lower()
    if option == "off":
        machine_working = False
    elif option == "report":
        coffeemachine.report()
    else:
        order = items.find_drink(option)
        if order != None:
            if coffeemachine.is_resource_sufficient(order):
                if money.make_payment(order.cost):
                    coffeemachine.make_coffee(order)
            else:
                print("Sorry, insuficient resources!")
        else:
            print(f"Please enter a valid order from {items.get_items()}")
