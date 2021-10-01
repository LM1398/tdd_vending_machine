from vending_machine.vending_machine import VendingMachine
from vending_machine.drinks import Drinks


def test_init_drinks():
    vending_machine = VendingMachine()
    assert vending_machine.stock == {"Coke": 5, "Redbull": 5, "Water": 5}

