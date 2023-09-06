from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

take_order = Menu()
coffee_machine = CoffeeMaker()
money = MoneyMachine()


should_stop = False

while not should_stop:
    order = input(f"What would you like to have choose: ({take_order.get_items()}) : ").lower()
    # drink = take_order.find_drink(order)
    if order=='report':
        coffee_machine.report()
        money.report()
    elif order=='stop':
        should_stop=True
        print("GoodBye")
    else:
        drink = take_order.find_drink(order)
        if drink != None:
            if coffee_machine.is_resource_sufficient(drink):
                if money.make_payment(drink.cost):
                    coffee_machine.make_coffee(drink)

