from vending_machine.money import Money
from vending_machine.drinks import Drinks
from collections import Counter


class VendingMachine:
    def __init__(self):
        self.money_box = []
        self.change = []
        self.fridge = []
        self.stock = {}

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

    def add_drink(self, drink, amount):
        for x in range(amount + 1):
            if x < amount:
                self.fridge.append(drink.name)
        self.stock = Counter(self.fridge)
