from vending_machine.vending_machine import VendingMachine
from vending_machine.money import Money


def test_not_accepted():
    vending_machine = VendingMachine()
    vending_machine.insert(Money.M_10000)
    assert vending_machine.change == []
