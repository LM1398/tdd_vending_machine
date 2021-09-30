from vending_machine.vending_machine import VendingMachine
from vending_machine.drinks import Drinks


def test_new_stock():
    vending_machine = VendingMachine()
    coke = Drinks("coke", 120)
    vending_machine.add_drink(coke, 5)
    vending_machine.add_drink(coke, 5)
    assert vending_machine.stock == {"coke": 10}

