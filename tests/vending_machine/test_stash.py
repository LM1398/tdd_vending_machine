from vending_machine.vending_machine import VendingMachine
from vending_machine.drinks import Drinks
from vending_machine.money import Money


def test_stash():
    vending_machine = VendingMachine()
    redbull = Drinks("redbull", 200)
    vending_machine.add_drink(redbull, 5)
    vending_machine.insert(Money.M_1000)
    vending_machine.buy(redbull)
    assert vending_machine.stash == [Money.M_100, Money.M_100]
