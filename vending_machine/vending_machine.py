from vending_machine.money import Money
from vending_machine.drinks import Drinks


class VendingMachine:
    money_box = []
    change = []
    fridge = []

    def insert(cash):
        accepted = [
            Money.M_10,
            Money.M_50,
            Money.M_100,
            Money.M_500,
            Money.M_1000,
        ]
        if cash in accepted:
            VendingMachine.money_box.append(cash)
        else:
            VendingMachine.change.append(cash)

    def add_drink(drink):
        VendingMachine.fridge.append(drink.name)
