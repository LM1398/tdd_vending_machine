""" Contains class VendingMachine which is used to organize and group the other src files. 
"""

from vending_machine.money import Money
from vending_machine.drinks import Drinks


class VendingMachine:
    """ Main VendingMachine class to organize all of the different src files and classes.
    
    Attributes:
        money_box: A list where the approved types of currencies are inserted.
        change: A list where the unaccepted types of currencies as well as change from buying drinks are inserted.
        fridge: A list with the name of each drink that is inserted in the machine.
        stock: A dictionary that counts the amount of each drink in self.fridge.
        revenue: A list that counts the total revenue of the vending machine.
        accepted: A list of all the accepted types of currencies
        

    """

    def __init__(self):
        """Inits VendingMachine with moneybox, change, fridge, and stock.
        """
        self.money_box = []
        self.change = []
        self.fridge = []
        self.stock = {}
        self.stash = []
        self.revenue = 0
        self.accepted = [
            Money.M_1000,
            Money.M_500,
            Money.M_100,
            Money.M_50,
            Money.M_10,
        ]

    def insert(self, cash):
        """ Inserts money separates the types of money into accepted and not-accepted(change) and inserts them into the different lists.
        Args:
            cash (Money): Money.M_x instance
        """

        if cash in self.accepted:
            self.money_box.append(cash)
        else:
            self.change.append(cash)
            self.dispense()

    def add_drink(self, drink, amount):
        """add_drink is used to add a certain amount of drinks into the fridge list, and the stock counts the number of each drink.
        Args:
            drink (Drinks): instance of specific drink.
            amount (int): desired number of drinks to be added.
        """
        for _drink in range(1, amount + 1):
            if _drink <= amount:
                self.fridge.append(drink)
        self.stock[drink.name] = self.fridge.count(drink)

    def purchasable(self):

        """Returns which drinks are purchasable depending on how much money is inserted and which drinks are in the fridge.

        Args:
            drink (Drinks): instance of specific drink.

        Returns:
            purchasable: A list of the purchasable drinks.
        """
        total = 0
        purchasable = []
        for cash in self.money_box:
            total += cash.amount
        for _drink in set(self.fridge):
            if total >= _drink.price:
                purchasable.append(_drink.name)
        return purchasable

    def calculate_change(self, pay):
        """ Calculates the change return with the least amount of coins/bills 

        Args:
            pay (int): Amount of change that will be returned to the buyer.
        """
        for x in self.accepted:
            returned_money = pay // x.amount
            if returned_money >= 1:
                for amount in range(1, returned_money + 1):
                    self.change.append(x)
                pay -= x.amount * (returned_money)

        return self.dispense()

    def dispense(self):
        """Returns the change after buying a drink and clears self.change

        Returns:
            disepnse: A list containing self.change
        """
        if len(self.change) == 0:
            dispense = 0
        else:
            dispense = [x for x in self.change]
        self.change.clear()
        return dispense

    def buy(self, drink):
        """ Method to buy drinks from the vending machine.
        If purchasable() returns that the drink is purchasable, the money is inserted into the stash and the change is calculated by subracting the
        drink price from the amount of money inserted. The change calculates and returns the least amount of coins.
        The drink is then removed from the fridge and the total revenue is calcualted.

        Args:
            drink (Drinks): instance of specific drink.
        """
        total = 0
        if drink.name not in VendingMachine.purchasable(self):
            print(f"{drink.name} is not purchasable")
        else:

            price = drink.price
            for currency in self.accepted:
                if price // currency.amount >= 1:
                    for amount in range(1, price // currency.amount + 1):
                        self.stash.append(currency)
                    price -= currency.amount * amount

            for cash in self.money_box:
                total += cash.amount
            pay = total - drink.price
        return self.calculate_change(pay)
