""" Contains class VendingMachine which is used to organize and group the other src files. 
"""

from vending_machine.money import Money
from vending_machine.drinks import Drinks
from collections import Counter


class VendingMachine:
    """ Main VendingMachine class to organize all of the different src files and classes.
    
    Attributes:
        money_box: A list where the approved types of currencies are inserted.
        change: A list where the unaccepted types of currencies as well as change from buying drinks are inserted.
        fridge: A list with the name of each drink that is inserted in the machine.
        stock: A dictionary that counts the amount of each drink in self.fridge.

    """

    def __init__(self):
        """Inits VendingMachine with moneybox, change, fridge, and stock.
        """
        self.money_box = []
        self.change = []
        self.fridge = []
        self.stock = {}

    def insert(self, cash):
        """ Inserts money separates the types of money into accepted and not-accepted(change) and inserts them into the different lists.

        Args:
            cash (Money): Money.M_x instance
        """
        accepted = [
            Money.M_10,
            Money.M_50,
            Money.M_100,
            Money.M_500,
            Money.M_1000,
        ]
        if cash in accepted:
            self.money_box.append(cash)
        else:
            self.change.append(cash)

    def add_drink(self, drink, amount):
        """add_drink is used to add a certain amount of drinks into the fridge list, and the stock counts the number of each drink.
        Args:
            drink (Drinks): instance of specific drink.
            amount (int): desired number of drinks to be added.
        """
        for _drink in range(1, amount + 1):
            if _drink <= amount:
                self.fridge.append(drink.name)
        self.stock = Counter(self.fridge)

    def purchasable(self, drink):
        """Returns whether a drink is purchasable depending on how much money is inserted and whether the drink is in the fridge.

        Args:
            drink (Drinks): instance of specific drink

        Returns:
            str: "drink is purchasable" or "drink is not in stock"
        """
        total = 0
        for cash in self.money_box:
            total += cash.amount
            if total > drink.price:
                pass
            else:
                return f"Insert additional money: {drink.price - total} yen"
        if drink.name in self.fridge:
            return "coke is purchasable"
        else:
            return "coke is not in stock"

