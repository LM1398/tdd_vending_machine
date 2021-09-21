from vending_machine.vending_machine import VendingMachine
from vending_machine.drinks import Drinks


def testing_drink():
    coke = Drinks("coke", 120)
    VendingMachine.add_drink(coke)
    assert coke.name == "coke"
    assert coke.price == 120
    assert VendingMachine.fridge == ["coke"]
