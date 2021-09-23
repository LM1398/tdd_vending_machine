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
        """list where the approved types of currencies are inserted
        """
        self.change = []
        """list where the unaccepted types of currencies are inserted (in future will also include change from buying drinks)
        """
        self.fridge = []
        """list with the name of each drink that is inserted in the machine"
        """
        self.stock = {}
        """dictionary that counts the amount of each drink in self.fridge"
        """

    def insert(cash):
        """ insert separates the types of money into accepted and not-accepted(change) and inserts them into the different lists.

        Args:
            cash (instance): Money.M_x instance from class Money in money.py
        """
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
        """add_drink is used to add a certain amount of drinks into the fridge list, and the stock counts the number of each drink.

        Args:
            drink (instance): instance of specific drink created using class Drink in drink.py
            amount (int): desired number of drinks to be added
        """
        for x in range(amount + 1):
            if x < amount:
                self.fridge.append(drink.name)
        self.stock = Counter(self.fridge)
