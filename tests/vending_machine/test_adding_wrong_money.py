from vending_machine.money import Money
from vending_machine.vending_machine import VendingMachine


def test_insert():
    VendingMachine.insert(Money.M_1)
    VendingMachine.insert(Money.M_5)
    VendingMachine.insert(Money.M_10)
    VendingMachine.insert(Money.M_50)
    VendingMachine.insert(Money.M_100)
    VendingMachine.insert(Money.M_500)
    VendingMachine.insert(Money.M_1000)
    VendingMachine.insert(Money.M_2000)
    VendingMachine.insert(Money.M_10000)

    assert VendingMachine.money_box == [
        Money.M_10,
        Money.M_50,
        Money.M_100,
        Money.M_500,
        Money.M_1000,
    ]
    assert VendingMachine.change == [Money.M_1, Money.M_5, Money.M_2000, Money.M_10000]
