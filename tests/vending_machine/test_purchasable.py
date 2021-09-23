from vending_machine.money import Money
from vending_machine.drinks import Drinks
from vending_machine.vending_machine import VendingMachine


def test_purchasable():
    coke = Drinks("coke", 120)
    vending_machine = VendingMachine()
    vending_machine.insert(Money.M_500)
    vending_machine.add_drink(coke, 3)
    assert vending_machine.purchasable(coke) == "coke is purchasable"


def test_more_money():
    coke = Drinks("coke", 120)
    vending_machine = VendingMachine()
    vending_machine.insert(Money.M_10)
    vending_machine.add_drink(coke, 3)
    assert vending_machine.purchasable(coke) == "Insert additional money: 110 yen"


def test_not_in_stock():
    coke = Drinks("coke", 120)
    vending_machine = VendingMachine()
    vending_machine.insert(Money.M_1000)
    assert vending_machine.purchasable(coke) == "coke is not in stock"
