""" Contains class VendingMachine which is used to organize and group the other src files. 
"""

from vending_machine.money import Money
from vending_machine.drinks import Drinks
from collections import Counter


class VendingMachine:
    """ Main class to organize all of the different src files and classes.
    """

    def __init__(self):
        """Used to create instances to insert the drink and money instances from the other classes (money.py and drinks.py).
        """
        self.money_box = []
        """list where the approved types of currencies are inserted.
        """
        self.change = []
        """list where the change from buying drinks as well as currencies that aren't accepted are inserted.
        """
        self.fridge = []
        """list with the name of each drink that is inserted in the machine.
        """
        self.stock = {}
        """dictionary that counts the amount of each drink in self.fridge.
        """
        self.stash = []
        """list that keeps all of the money used to buy drinks.
        """

        self.revenue = []
        """list that counts the total revenue of the vending machine.
        """

    def insert(self, cash):
        """ insert separates the types of money into accepted and not-accepted(change) and inserts them into the different lists.
        Args:
            cash (Money): Money.M_x instance from class Money in money.py.
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
            drink (instance): instance of specific drink created using class Drink in drink.py.
            amount (int): desired number of drinks to be added.
        """
        for _drink in range(1, amount + 1):
            if _drink <= amount:
                self.fridge.append(drink.name)
        self.stock = Counter(self.fridge)

    def purchasable(self, drink):
        """Returns whether a drink is purchasable depending on how much money is inserted and whether the drink is in fridge.

        Args:
            drink ([instance]): instance of specific drink created using class Drink in drink.py.

        Returns:
            [string]: "drink is purchasable" or "drink is not in stock".
        """
        total = 0
        for cash in self.money_box:
            total += cash.amount
            if total > drink.price:
                pass
            else:
                return f"Insert additional money: {drink.price - total} yen"
        if drink.name in self.fridge:
            return f"{drink.name} is purchasable"
        else:
            return f"{drink.name} is not in stock"

    def calculate_change(self, pay):
        """ Calculates the change return with the least amount of coins/bills 

        Args:
            pay (int): Amount of change that will be returned to the buyer.
        """
        money = [Money.M_1000, Money.M_500, Money.M_100, Money.M_50, Money.M_10]
        for x in money:
            at_least_one = pay // x.amount
            if at_least_one >= 1:
                for amount in range(1, at_least_one + 1):
                    if amount <= at_least_one:
                        self.change.append(x)
                pay -= x.amount * (at_least_one)

    def buy(self, drink):
        """ Method to buy drinks from the vending machine.
        If purchasable() returns that the drink is purchasable, the money is inserted into the stash and the change is calculated by subracting the
        drink price from the amount of money inserted. The change calculates and returns the least amount of coins.
        The drink is then removed from the fridge and the total revenue is calcualted.

        Args:
            drink ([instance]): instance of specific drink created using class Drink in drink.py.
        """
        total = 0
        if self.purchasable(drink) != f"{drink.name} is purchasable":
            print(f"{drink.name} is not purchasable")
        else:
            if drink.price == 120:
                self.stash.append(Money.M_100)
                self.stash.append(Money.M_10)
                self.stash.append(Money.M_10)
            else:
                pass
            for cash in self.money_box:
                total += cash.amount
            pay = total - drink.price
            self.calculate_change(pay)
            self.fridge.remove(drink.name)
            self.revenue = sum(x.amount for x in self.stash)
