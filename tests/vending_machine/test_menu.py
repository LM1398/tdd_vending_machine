from vending_machine.vending_machine import VendingMachine
from vending_machine.drinks import Drinks


def test_buy():
    vending_machine = VendingMachine()
    coke = Drinks("Coke", 120)
    redbull = Drinks("Redbull", 120)
    water = Drinks("Water", 120)
    vending_machine.add_drink(coke, 5)
    vending_machine.add_drink(redbull, 5)
    vending_machine.add_drink(water, 5)
    assert vending_machine.menu() == {"Coke", "Redbull", "Water"}
