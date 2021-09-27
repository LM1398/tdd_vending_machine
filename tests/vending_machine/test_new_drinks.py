from vending_machine.vending_machine import VendingMachine
from vending_machine.money import Money
from vending_machine.drinks import Drinks
from collections import Counter


def test_water():
    vending_machine = VendingMachine()
    water = Drinks("Water", 100)
    vending_machine.add_drink(water, 5)
    assert vending_machine.stock == Counter({"Water": 5})


def test_redbull():
    vending_machine = VendingMachine()
    redbull = Drinks("RedBull", 200)
    vending_machine.add_drink(redbull, 5)
    print(vending_machine.stock)
    assert vending_machine.stock == Counter({"RedBull": 5})

