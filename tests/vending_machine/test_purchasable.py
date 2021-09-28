from vending_machine.money import Money
from vending_machine.drinks import Drinks
from vending_machine.vending_machine import VendingMachine


def test_purchasable():
    coke = Drinks("Coke", 120)
    redbull = Drinks("Redbull", 200)
    water = Drinks("Water", 100)
    vending_machine = VendingMachine()
    vending_machine.add_drink(coke, 3)
    vending_machine.add_drink(redbull, 3)
    vending_machine.add_drink(water, 3)
    vending_machine.insert(Money.M_100)
    vending_machine.insert(Money.M_10)
    vending_machine.insert(Money.M_10)
    assert vending_machine.purchasable() == ["Water", "Coke"]
