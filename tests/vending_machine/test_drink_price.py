from vending_machine.vending_machine import VendingMachine
from vending_machine.drinks import Drinks


def test_drink_price():
    coke = Drinks("coke", 120)
    assert coke.price == 120
