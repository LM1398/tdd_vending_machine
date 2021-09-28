from vending_machine.vending_machine import VendingMachine
from vending_machine.money import Money
from vending_machine.drinks import Drinks


def test_buy():
    coke = Drinks("coke", 120)
    vending_machine = VendingMachine()
    vending_machine.insert(Money.M_1000)
    vending_machine.insert(Money.M_1000)
    vending_machine.add_drink(coke, 5)
    assert vending_machine.buy(coke) == [
        Money.M_1000,
        Money.M_500,
        Money.M_100,
        Money.M_100,
        Money.M_100,
        Money.M_50,
        Money.M_10,
        Money.M_10,
        Money.M_10,
    ]


def test_no_change():
    water = Drinks("Water", 100)
    vending_machine = VendingMachine()
    vending_machine.insert(Money.M_100)
    vending_machine.add_drink(water, 5)
    assert vending_machine.buy(water) == 0
