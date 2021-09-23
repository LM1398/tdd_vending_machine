    """ Contains money_box,change, fridge, and stock to organize money and drinks.
insert method: inserts money from money.py into change and money_box.
add_drink: adds drink from drink.py into fridge and stock.
    """

from vending_machine.money import Money
from vending_machine.drinks import Drinks
from collections import Counter


class VendingMachine:
    """ Main class to organize all of the different src files and classes.
    __init__ is used to create instances to insert the drink and money instances from the other classes (money.py and drinks.py)
    insert separates the types of money into accepted and not-accepted(change) and inserts them into the different lists
    add_drink is used to add a certain amount of drinks into the fridge list, and the stock counts the number of each drink
    """
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
