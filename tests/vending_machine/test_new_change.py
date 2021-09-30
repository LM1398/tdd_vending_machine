from vending_machine.vending_machine import VendingMachine
from vending_machine.money import Money
from vending_machine.drinks import Drinks


def test_new_change():
    coke = Drinks("coke", 120)
    vending_machine = VendingMachine()
    vending_machine.add_drink(coke, 5)
    vending_machine.insert(Money.M_100)
    vending_machine.insert(Money.M_50)
    print(vending_machine.buy(coke))
    assert vending_machine.buy(coke) == [Money.M_10, Money.M_10, Money.M_10]
