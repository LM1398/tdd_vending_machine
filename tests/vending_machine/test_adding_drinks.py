from vending_machine.vending_machine import VendingMachine
from vending_machine.drinks import Drinks
from collections import Counter


def testing_drink():
    vending_machine = VendingMachine()
    coke = Drinks("coke", 120)
    vending_machine.add_drink(coke, 5)
    assert vending_machine.stock == Counter({"coke": 5})

