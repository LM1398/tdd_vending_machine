from vending_machine.money import Money
from vending_machine.vending_machine import VendingMachine


def test_insert():
    VendingMachine.insert(Money.M_100)
    VendingMachine.insert(Money.M_500)
    VendingMachine.insert(Money.M_1000)
    assert VendingMachine.money_box == 1600

