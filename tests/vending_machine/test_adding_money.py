from vending_machine.money import Money
from vending_machine.vending_machine import VendingMachine


def test_insert():
    VendingMachine.insert(Money.M_100)
    assert VendingMachine.money_box == 100

